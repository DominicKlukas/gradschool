---
tags:
  - technical_library
title: Continual Vision-based Reinforcement Learning with Group Symmetries
authors: Shiqi Liu, Mengdi Xu, Piede Huang, Yongkang Liu, Kentaro Oguchi, Ding Zhao
bibtex: "@misc{liu2023continualvisionbasedreinforcementlearning,      title={Continual Vision-based Reinforcement Learning with Group Symmetries},       author={Shiqi Liu and Mengdi Xu and Piede Huang and Yongkang Liu and Kentaro Oguchi and Ding Zhao},      year={2023},      eprint={2210.12301},      archivePrefix={arXiv},      primaryClass={cs.LG},      url={https://arxiv.org/abs/2210.12301}, }"
pretty_cite:
link: https://doi.org/10.48550/arXiv.2210.12301
topics: Continual Reinforcement Learning, Task Delineation, RL, Equivariance
reading_lists:
projects:
type:
to_read: false
stars:
---
Continual RL is when you sequentially learn a series of tasks, without losing the ability to do all the tasks that you have learned before. In order to do this, you need to do something called task delineation, where you 
They cite papers (24-27) which define homomorphisms of mdps to smaller mdps, so that you solve the smaller mdp and in doing so solve the bigger one. Group equivariance is a form of such a symmetry.
- A previous paper done by the same people trains and keeps a set of experts. With a latent variable, determines which expert is most likely to correspond to the current task, or whether a new actor has to be trained.
- This paper does a similar thing. It uses equivariant PPO architectures for the experts. It uses a group invariant task grouper as well, computing the difference between the given task and tasks seen before to choose an expert or choose to create a new expert.