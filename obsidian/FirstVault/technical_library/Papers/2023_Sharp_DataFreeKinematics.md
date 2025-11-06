---
tags:
  - technical_library
title: Data-Free Learning of Reduced-Order Kinematics
authors: Nicholas Sharp, Cristian Romero, Alec Jacobson, Etienne Vouga, Paul G. Kry, David I.W. Levin, Justin Solomon
bibtex: "@misc{sharp2023datafreelearningreducedorderkinematics,      title={Data-Free Learning of Reduced-Order Kinematics},       author={Nicholas Sharp and Cristian Romero and Alec Jacobson and Etienne Vouga and Paul G. Kry and David I. W. Levin and Justin Solomon},      year={2023},      eprint={2305.03846},      archivePrefix={arXiv},      primaryClass={cs.GR},      url={https://arxiv.org/abs/2305.03846}, }"
pretty_cite:
link: https://doi.org/10.48550/arXiv.2305.03846
topics: Physics
reading_lists:
projects:
type:
to_read: false
stars:
---
You have a function, $E(x)$, that takes a state of your system, described as $x \in \mathbb{R}^n$, to some energy level. Then, you train a neural network from $\mathbb{R}^d$ to $\mathbb{R}^n$. You initialize it to be random, but your loss function encourages low energy states, and a diversity function encourages states to be relatively unique (not constantly at the global minimum). This can then help you see what the low energy states of the system are (they will be the range of your function in $\mathbb{R}^n$) but of course won't tell you anything about the dynamics of the system.