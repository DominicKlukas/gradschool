---
tags:
  - technical_library
title: "DiffTaichi: Differentiable Programming for Physical Simulation"
authors: Yuanming Hu, Luke Anderson, Tzu-Mao Li, Qi Sun, Nathan Carr, Jonathan Ragan-Kelley, Frédo Durand
bibtex: "@misc{hu2020difftaichidifferentiableprogrammingphysical,      title={DiffTaichi: Differentiable Programming for Physical Simulation},       author={Yuanming Hu and Luke Anderson and Tzu-Mao Li and Qi Sun and Nathan Carr and Jonathan Ragan-Kelley and Frédo Durand},      year={2020},      eprint={1910.00935},      archivePrefix={arXiv},      primaryClass={cs.LG},      url={https://arxiv.org/abs/1910.00935}, }"
pretty_cite:
link: https://arxiv.org/abs/1910.00935
topics: Differentiable Physical Simulators
reading_lists:
projects:
type:
to_read: false
stars:
---
The motivation is as follows
	1. You have a policy, and a reward function, and you want to optimize a trajectory to maximize your reward.
	2. In the real world, you often have to do repeated runs each time you want to test another trajectory.
	3. In this case, you can compute the gradients of your trajectory with respect to the parameters of your policy, and in doing so compute the gradient of your accumulated reward directly.
   The paper introduces a new programming language/compiler which takes a simple implementation of a physics simulator and creates fast, differentiable simulator code out of it.