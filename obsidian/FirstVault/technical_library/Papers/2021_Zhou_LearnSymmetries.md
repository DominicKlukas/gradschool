---
tags:
  - technical_library
title: Meta-Learning Symmetries by Reparameterization
authors: Allan Zhou, Tom Knowles, Chelsea Finn
bibtex: "@misc{zhou2021metalearningsymmetriesreparameterization,      title={Meta-Learning Symmetries by Reparameterization},       author={Allan Zhou and Tom Knowles and Chelsea Finn},      year={2021},      eprint={2007.02933},      archivePrefix={arXiv},      primaryClass={cs.LG},      url={https://arxiv.org/abs/2007.02933}, }"
pretty_cite:
link: https://doi.org/10.48550/arXiv.2007.02933
topics: Equivariance, DL, Symmetry Breaking
reading_lists:
projects: SDM Course Project
type:
to_read: true
stars:
---
Let $W$ be the linear, fully connected weight matrix of an MLP. Then, we can flatten $W$ into an $nm$ vector. Now, we can have this flattened $W$ be a linear combination of $nm$ vectors, and write it as $U \in \mathbb{R}^{nm \times k}$, parameterizing it with another vector, $v$. In particular, the idea is that $U$ will be learned such that each column is an equivariance preserving layer, so $v$ is a linear combination of different such columns. Then, when we train our network, we take turns, learning $v$, and learning $U$, so that the right equivariance is learned.