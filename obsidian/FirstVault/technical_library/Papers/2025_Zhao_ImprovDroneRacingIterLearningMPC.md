---
tags:
  - technical_library
title: Improving Drone Racing Performance Through Iterative Learning MPC
authors: Haocheng Zhao, Niklas Schlüter, Lukas Brunke, and Angela P. Schoellig
bibtex: "@misc{zhao2025improvingdroneracingperformance,      title={Improving Drone Racing Performance Through Iterative Learning MPC},       author={Haocheng Zhao and Niklas Schlüter and Lukas Brunke and Angela P. Schoellig},      year={2025},      eprint={2508.01103},      archivePrefix={arXiv},      primaryClass={cs.RO},      url={https://arxiv.org/abs/2508.01103}, }"
pretty_cite:
link: https://doi.org/10.48550/arXiv.2508.01103
topics:
reading_lists:
projects: CoCo Course Project
type:
to_read: false
stars:
---
## Introduction
- Drone racing is a tough but useful problem.
- RL is good but suffers from sim to real difficulties. MPC is more consistent.
- LMPC combines MPC and ILC (iterative learning control)
- In this paper:
	- Adapt const function, so time of a lap is balanced with centerline adherance in order to ensure we are getting through the gates
	- Modify the local safe set to prevent excessive aggression
	- Safety constraints without singularities and numerical integration errors caused by Frenet frame transformations
## Related Works
- Flatness based methods: we determine a function between a simpler input (change in velocity) and the inputs that we have.
- In MPC, we have a safe set which the plant is constrained to act within, ensuring safety. However, computing these sets is difficult. LMPC uses previously successful maneuvers.
	- Previous implementations have made improvements, showing the potential of LMPC for drone racing, but 
## Problem setting
![[Screenshot2025-10-07_15-08-09.png]]
- This is the control problem.
- Every single gate has it's own co-ordinate frame, where the $z$ axis is perpendicular to the face of the gate in its frame.
- $p_{i}^{t_{n}i}$ is the position of the gate's origin ($t_{n} i$) in the inertial frame $i$.
- $R_{it_{n}}$ is a transformation between the co-ordinate frames.
- $\mathbb{T}_{n}$ is a plane in the $x$-$y$ plane, defining the shape of the gate.
- The third constraint on velocity essentially forces the drone to fly through the gate.
## Preliminaries
Problem with Euler angles: we rotate about rotated axes: if you rotate to a position where axes are lined up,