---
tags:
  - technical_library
title: Symmetry Detection in Trajectory Data for More Meaningful Reinforcement Learning Representations
authors: Marissa D'Alonzo, Rebecca Russell
bibtex: "@misc{dalonzo2022symmetrydetectiontrajectorydata,      title={Symmetry Detection in Trajectory Data for More Meaningful Reinforcement Learning Representations},       author={Marissa D'Alonzo and Rebecca Russell},      year={2022},      eprint={2211.16381},      archivePrefix={arXiv},      primaryClass={cs.LG},      url={https://arxiv.org/abs/2211.16381}, }"
pretty_cite:
link: https://doi.org/10.48550/arXiv.2211.16381
topics: Equivariance, RL, Symmetry Detection
reading_lists:
projects: Equivariant Learning
type:
to_read: false
stars:
---
They start with candidate transformations, transform their original trajectories, then use a discriminator network to see if it can learn the difference between the transformed and original trajectories. If the original trajectories were sampled from a symmetric distribution, the two datasets (transformed and original) will be the same.
