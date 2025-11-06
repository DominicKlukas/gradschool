---
tags:
  - technical_library
title: A Practical Guide for Incorporating Symmetry in Diffusion Policy
authors: Dian Wang, Boce Hu, Shuran Song, Robin Walters, Robert Platt
bibtex: "@misc{wang2025practicalguideincorporatingsymmetry,      title={A Practical Guide for Incorporating Symmetry in Diffusion Policy},       author={Dian Wang and Boce Hu and Shuran Song and Robin Walters and Robert Platt},      year={2025},      eprint={2505.13431},      archivePrefix={arXiv},      primaryClass={cs.RO},      url={https://arxiv.org/abs/2505.13431}, }"
pretty_cite:
link: https://doi.org/10.48550/arXiv.2505.13431
topics: Equivariance, Diffusion Policies
reading_lists:
projects:
type:
to_read: false
stars:
---
They propose three techniques to augment diffusion models without making them fully equivariant:
- Just replace the CNN with an equivariant CNN
- Compute the relative trajectories, applying the inverse of the SE3 transformation that gets you to your initial state
- Create an equivariant function from a non-equivariant function, in the case of a finite group, using the following technique:
$$
\Psi(x) = \frac{1}{|G|} \sum_{g \in G}  \rho_{y}(g) \Phi(\rho_{x}(g)^{-1}x)
$$
Then, the resulting function will be equivariant!

These modifications in the context of behavioral cloning for robotics manipulation has significant performance gains over regular behavior cloning with diffusion models.