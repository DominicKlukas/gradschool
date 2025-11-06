---
tags:
  - technical_library
title: "How to Learn and Generalize From Three Minutes of Data: Physics-Constrained and Uncertainty-Aware Neural Stochastic Differential Equations"
authors: Franck Djeumou, Cyrus Neary, Ufuk Topcu
bibtex: "@misc{djeumou2023learngeneralizeminutesdata,      title={How to Learn and Generalize From Three Minutes of Data: Physics-Constrained and Uncertainty-Aware Neural Stochastic Differential Equations},       author={Franck Djeumou and Cyrus Neary and Ufuk Topcu},      year={2023},      eprint={2306.06335},      archivePrefix={arXiv},      primaryClass={cs.LG},      url={https://arxiv.org/abs/2306.06335}, }"
pretty_cite:
link: https://doi.org/10.48550/arXiv.2306.06335
topics: Robotics, SDE, PDE, RL
reading_lists:
projects:
type:
to_read: false
stars:
---
They use model predictive control (that is, where they use their SDE to predict rewards from actions). They train the SDE on a limited amount of data, by determining the structure of f to include physics, and letting the noise term g be controlled by how far states are from training data. 