---
tags:
  - technical_library
title: "PhysTwin: Physics-Informed Reconstruction and Simulation of Deformable Objects from Videos"
authors: Hanxiao Jiang, Hao-Yu Hsu, Kaifeng Zhang, Hsin-Ni Yu, Shenlong Wang, Yunzhu Li
bibtex: "@misc{jiang2025phystwinphysicsinformedreconstructionsimulation,      title={PhysTwin: Physics-Informed Reconstruction and Simulation of Deformable Objects from Videos},       author={Hanxiao Jiang and Hao-Yu Hsu and Kaifeng Zhang and Hsin-Ni Yu and Shenlong Wang and Yunzhu Li},      year={2025},      eprint={2503.17973},      archivePrefix={arXiv},      primaryClass={cs.CV},      url={https://arxiv.org/abs/2503.17973}, }"
pretty_cite:
link: https://arxiv.org/abs/2503.17973
topics: Physics, Gaussian Splatting, Simulation, Video, Graphics
reading_lists:
projects: "[[Physics Aware Learning]]"
type:
to_read: false
stars:
---
XR stands for extended reality, so VR, AR, or Mixed Reality.
Dynamic 3D method: creating a 3D model from videos, which captures the model at each frame in the video.

What it does?
- Builds a PhysTwin: captures the geometry, appearance, and physical properties of a measured object, which can be used to do physical simulation and future rendering.
- Resimulation: determine parameters/forces from a video.
How it does it?
- 3D Generative Models to help you create geometry from sparse cameras.
	- Zero order optimization for some properties (topology, geometry, collision parameters, homogeneous spring stiffness) that don't have gradients
	- First order optimization when gradients are available: spring stiffness/collision params at specific points.
- For rendering, attach to each mesh node of geometry a Gaussian, which is used to render the model.
- The loss has multiple terms: appearance (rendered image from Gaussian splats), the mesh, and the motion computed by the physics simulation are all minimized.
What is required?
- 3 RGB-D cameras. Every pixel has a distance measured.
- Object material:  Works on ropes, stuffed animals, cloth. (Rigid, and slightly deformable.)