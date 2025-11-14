---
tags:
  - technical_library
title: The Surprising Effectiveness of Equivariant Models in Domains with Latent Symmetry
authors: Dian Wang, Jung Yeon Park, Neel Sortur, Lawson L.S. Wong, Robin Walters, Robert Platt
bibtex: "@misc{wang2023surprisingeffectivenessequivariantmodels,      title={The Surprising Effectiveness of Equivariant Models in Domains with Latent Symmetry},       author={Dian Wang and Jung Yeon Park and Neel Sortur and Lawson L. S. Wong and Robin Walters and Robert Platt},      year={2023},      eprint={2211.09231},      archivePrefix={arXiv},      primaryClass={cs.LG},      url={https://arxiv.org/abs/2211.09231}, }"
pretty_cite:
link: https://doi.org/10.48550/arXiv.2211.09231
topics: Equivariance, DL, Latent Symmetry
reading_lists:
projects:
type:
to_read: false
stars:
---
Questions
- When is it a good/bad idea to use symmetry?

Definitions
- Correct equivariance: model correctly models the problem symmetry
- Incorrect equivariance: model symmetry intereferes with the problem symmetry
- Extrinsic equivariance: Model symmetry transforms the input data to out-of-distribution data

They tested the following empirically:
- A classification function which compares the amount items have been rotated in images.
	- They corrupt the symmetry such that the models still have extrinsic symmetry, and show that when symmetry is corrupted in this manner, the equivariant models still perform well
	- When there is incorrect equivariance, then they show that the problem symmetry is worse.
