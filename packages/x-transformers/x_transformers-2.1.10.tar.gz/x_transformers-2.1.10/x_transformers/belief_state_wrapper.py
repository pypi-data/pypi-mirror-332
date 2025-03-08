
# Belief State Transformer

# https://arxiv.org/abs/2410.23506
# https://www.youtube.com/watch?v=aqhbRtB2Fyg

from __future__ import annotations

import torch
from torch.autograd import Function
from torch.nn import Module, ModuleList
from torch import nn, cat, stack, tensor, arange, cartesian_prod
import torch.nn.functional as F

from x_transformers.x_transformers import (
    Decoder,
    TransformerWrapper
)

import einx
from einops import rearrange, repeat

# helper functions

def exists(v):
    return v is not None

def default(v, d):
    return v if exists(v) else d

# wrappers

class BeliefStateWrapper(Module):
    """
    Figure 13. in https://arxiv.org/abs/2410.23506
    """

    def __init__(
        self,
        forward_decoder: TransformerWrapper,
        backward_decoder: TransformerWrapper | None = None,
        train_frac_forward_backward_pairs: float = 1.,
        text_head: Module | None = None,
        backward_ar_loss_weight: float = 1. # can weigh the training of the backwards decoder differently, perhaps fwd/bwd have a shared backbone etc etc
    ):
        super().__init__()
        backward_decoder = default(backward_decoder, forward_decoder) # if backward decoder not set, use the same transformer, assume it knows how to switch gears based on suffix token

        assert forward_decoder.emb_dim == backward_decoder.emb_dim, 'forward and backwards model must have the same embedding dimension'
        assert forward_decoder.num_tokens == backward_decoder.num_tokens, 'forward and backwards model must have the same number of tokens'

        dim = forward_decoder.emb_dim
        num_tokens = forward_decoder.num_tokens

        # the suffix token

        self.suffix_token = nn.Parameter(torch.zeros(dim))
        nn.init.normal_(self.suffix_token, std = 0.02)

        # the text prediction head, which predicts for the combinations of prefix and suffix the next and previous token for forwards and backward sequences

        if not exists(text_head):
            text_head = nn.Sequential(
                nn.Linear(dim * 2, dim),
                nn.LeakyReLU(),
                nn.Linear(dim, num_tokens * 2),
            )

        self.text_head = text_head

        # the two decoders, one which is causal forward, the other causal backwards

        self.forward_decoder = forward_decoder
        self.backward_decoder = backward_decoder

        # what fraction of forward backward pairs to train on
        # for further memory efficiency

        assert 0 < train_frac_forward_backward_pairs <= 1.
        self.train_frac_fb_pairs = train_frac_forward_backward_pairs
        self.needs_subsample_fb_pairs = train_frac_forward_backward_pairs < 1.

        # loss weighting

        self.backward_ar_loss_weight = backward_ar_loss_weight
        self.needs_loss_weight = backward_ar_loss_weight != 1.

        self.register_buffer('loss_weights', tensor([1., self.backward_ar_loss_weight]))

    def forward(
        self,
        seq,
        backward = True
    ):
        batch, seq_len, device = *seq.shape, seq.device

        # forward autoregressive

        forward_embeds = self.forward_decoder(seq, return_embeddings = True)

        # backward autoregressive

        backward_seq = seq.flip(1)

        suffix_tokens = repeat(self.suffix_token, 'd -> b 1 d', b = batch)

        backward_embeds = self.backward_decoder(
            backward_seq,
            prepend_embeds = suffix_tokens,
            return_embeddings = True
        )

        backward_embeds = backward_embeds.flip(1)

        # trick to reduce memory on backwards pass

        orig_forward_embeds, forward_embeds = forward_embeds, forward_embeds.detach()
        orig_backward_embeds, backward_embeds = backward_embeds, backward_embeds.detach()

        forward_embeds.requires_grad_()
        backward_embeds.requires_grad_()

        # belief state objective

        seq_arange = arange(seq_len, device = device)

        fb_pairs = cartesian_prod(seq_arange, seq_arange)

        # filter down to valid pairs, as in figure 11
        # f - forward, b - backward, i - indices

        fi, bi = fb_pairs.unbind(dim = -1)
        valid_mask = (bi - fi) >= 2

        fb_pairs = fb_pairs[valid_mask]

        # maybe subsample fb pairs

        if self.needs_subsample_fb_pairs:
            num_pairs = fb_pairs.shape[0]

            num_subsampled = max(int(num_pairs * self.train_frac_fb_pairs), 1)

            rand_subsampled_indices = torch.randperm(num_pairs, device = device)[:num_subsampled]

            fb_pairs = fb_pairs[rand_subsampled_indices]

        # get labels for both

        fi, bi = fb_pairs.unbind(dim = -1)

        labels_fi, labels_bi = (fi + 1), bi

        forward_labels, backward_labels = seq[:, fi], seq[:, bi]
        labels = stack((forward_labels, backward_labels), dim = -1)

        # get the forward and backward embedding pairs and feed them through the text head for both forward and backward predictions

        fb_embeds = cat((
            forward_embeds[:, fi],
            backward_embeds[:, bi]
        ), dim = -1)

        logits = self.text_head(fb_embeds)

        # cross entropy loss

        fb_loss = F.cross_entropy(
            rearrange(logits, 'b n (fb l) -> b l (fb n)', fb = 2),
            rearrange(labels, 'b n fb -> b (fb n)'),
            reduction = 'none' if self.needs_loss_weight else 'mean'
        )

        # maybe loss weighting

        if self.needs_loss_weight:
            fb_loss = rearrange(fb_loss, 'b (fb n) -> b fb n', fb = 2)
            fb_loss = einx.multiply('b fb n, fb', fb_loss, self.loss_weights)
            fb_loss = fb_loss.mean()

        # backwards

        orig_backward = getattr(fb_loss, 'backward')

        def patched_backward_fn(*args, **kwargs):
            orig_backward(*args, **kwargs)
            orig_forward_embeds.backward(forward_embeds.grad)
            orig_backward_embeds.backward(backward_embeds.grad)

        # can allow the researcher to call .backward from the outside

        if backward:
            patched_backward_fn()
        else:
            setattr(fb_loss, 'backward', patched_backward_fn)

        return fb_loss
