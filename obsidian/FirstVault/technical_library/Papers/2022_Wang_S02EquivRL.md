---
tags:
  - technical_library
title: SO(2)-Equivariant Reinforcement Learning
authors: Dian Wang, Robin Walters, Robert Platt
bibtex: "@misc{wang2022mathrmso2equivariantreinforcementlearning,      title={$\\mathrm{SO}(2)$-Equivariant Reinforcement Learning},       author={Dian Wang and Robin Walters and Robert Platt},      year={2022},      eprint={2203.04439},      archivePrefix={arXiv},      primaryClass={cs.RO},      url={https://arxiv.org/abs/2203.04439}, }"
pretty_cite:
link: https://doi.org/10.48550/arXiv.2203.04439
topics: Equivariance, Robotics, RL, SAC
reading_lists:
projects: SDM Course Project
type:
to_read: false
stars:
---
Spatial action space: give end locations/angles.
Close-loop control: Cartesian delta motions, as in MetaWorld.
PyBullet seems to use spatial action space? But this paper claims in the intro to deal with close-loop control.
Visual motor control: using camera images to control your motors.
Feature map: hidden or output layer of neural network (transformation of data)


# Codebase
Here, I will write down my understanding of what each of the files that I read do
- utils/parameters.py
	- Runs at the start of the main.py file. Reads all of the arguments. Read to understand what arguments there are.
- helping_hands_rl_envs/helping_hands_rl_envs/base_env.py
	- This is the mother of all environments, where the basic variables are set up.