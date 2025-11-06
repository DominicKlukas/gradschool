---
tags:
  - technical_library
title: "PhysGaussian: Physics-Integrated 3D Gaussians for Generative Dynamics"
authors: Tianyi Xie, Zeshun Zong, Yuxing Qiu, Xuan Li, Yutao Feng, Yin Yang, Chenfanfu Jiang
bibtex: "@misc{xie2024physgaussianphysicsintegrated3dgaussians,      title={PhysGaussian: Physics-Integrated 3D Gaussians for Generative Dynamics},       author={Tianyi Xie and Zeshun Zong and Yuxing Qiu and Xuan Li and Yutao Feng and Yin Yang and Chenfanfu Jiang},      year={2024},      eprint={2311.12198},      archivePrefix={arXiv},      primaryClass={cs.GR},      url={https://arxiv.org/abs/2311.12198}, }"
pretty_cite:
link: https://doi.org/10.48550/arXiv.2311.12198
topics: Physics, Simulation
reading_lists:
projects:
type:
to_read: false
stars:
---
Learn parameters for a fixed number of 3D gaussians, placing these 3D Gaussian ellipsoids in space to try and reconstruct the original object (learning their positions for instance). These 3D Gaussians serve both as the building blocks for rendering new images and also as the basis for the physics simulation. The "splats" of the Gaussians aren't used, they are simply used to infer particle positions. Then, a physics simulator is applied, and after, Gaussians are generated again.