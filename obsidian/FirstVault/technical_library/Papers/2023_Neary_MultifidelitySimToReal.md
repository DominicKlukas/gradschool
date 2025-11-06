---
tags:
  - technical_library
title: A Multifidelity Sim-to-Real Pipeline for Verifiable and Compositional Reinforcement Learning
authors: Cyrus Neary, Christian Ellis, Aryaman Singh Samyal, Craig Lennon, Ufuk Topcu
bibtex: "@misc{neary2023multifidelitysimtorealpipelineverifiable,      title={A Multifidelity Sim-to-Real Pipeline for Verifiable and Compositional Reinforcement Learning},       author={Cyrus Neary and Christian Ellis and Aryaman Singh Samyal and Craig Lennon and Ufuk Topcu},      year={2023},      eprint={2312.01249},      archivePrefix={arXiv},      primaryClass={cs.RO},      url={https://arxiv.org/abs/2312.01249}, }"
pretty_cite:
link: https://doi.org/10.48550/arXiv.2312.01249
topics: Robotics, RL
reading_lists:
projects:
type:
to_read: false
stars:
---
Some terms:
- Autonomy Stack: often many different layers of decision making control that allows the robot to act autonomously. Perception, state estimation, planning, control, etc.
- SITL: Software In The Loop is when you run your entire autonomous robot software controller in a simulation of your robot, where the parts of your robot that will interface with the real world are simulated as well.

What the paper does
- You, the researcher, breaks the task down into subtasks. Each of these subtasks must have: a starting condition, and ending condition, and a failure condition.
- The conditions are states. Each subtask has a separate MDP defined for it, with the goal of getting from the starting states to the ending states avoiding the failure states.
- High level MDP computes the reliability of each of the subtasks as they go from one state to the next.
- One giant end-to-end RL policy cannot do this!
- Each subtask can be trained separately, on multiple levels with different data.


Questions
- Could it be the case that certain states within the enter condition have much lower chance of succeeding than others? How do you ensure that the enter conditions are the right "size"... that is, large enough to be useful, and small enough to be conclusive to reason about the success of the program?