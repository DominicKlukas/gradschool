---
tags:
  - technical_library
title: E(n) Equivariant Graph Neural Networks
authors: Victor Garcia Satorras, Emiel Hoogeboom, Max Welling
bibtex: "@misc{satorras2022enequivariantgraphneural,      title={E(n) Equivariant Graph Neural Networks},       author={Victor Garcia Satorras and Emiel Hoogeboom and Max Welling},      year={2022},      eprint={2102.09844},      archivePrefix={arXiv},      primaryClass={cs.LG},      url={https://arxiv.org/abs/2102.09844}, }"
pretty_cite:
link: https://doi.org/10.48550/arXiv.2102.09844
topics: Equivariance, DL, Graphs, Dynamical Systems
reading_lists:
projects:
type:
to_read: false
stars:
---
They develop a new architecture for graph neural networks.
They make the networks equivariant by doing message passing (computing a quantity $m_{ij}$ for the relationship between each of the two connected nodes and summing over them to make it permutation invariant, it is E2 equivariant by the nature of the way they compute the functions).
Invariant w.r.t. rotations, equivariant w.r.t. reflections, translations, and rotations.
We use MLPs to compute the message passing functions.
Other innovation: we can learn what edges are there using a soft-max function if necessary (there aren't too many nodes to have a fully connected graph be infeasible). Otherwise, could be computed by proximity (kNN).


Summary: I have a good understanding of the architecture.

Presentation flow:
- Introduce the type of problem you would want to apply this to.
- Introduce how these networks work.
- Introduce the results.