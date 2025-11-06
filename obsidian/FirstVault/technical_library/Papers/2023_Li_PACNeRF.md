---
tags:
  - technical_library
title: "PAC-NeRF: Physics Augmented Continuum Neural Radiance Fields for Geometry-Agnostic System Identification"
authors: Xuan Li, Yi-Ling Qiao, Peter Yichen Chen, Krishna Murthy Jatavallabhula, Ming Lin, Chenfanfu Jiang, Chuang Gan
bibtex: "@misc{li2023pacnerfphysicsaugmentedcontinuum,      title={PAC-NeRF: Physics Augmented Continuum Neural Radiance Fields for Geometry-Agnostic System Identification},       author={Xuan Li and Yi-Ling Qiao and Peter Yichen Chen and Krishna Murthy Jatavallabhula and Ming Lin and Chenfanfu Jiang and Chuang Gan},      year={2023},      eprint={2303.05512},      archivePrefix={arXiv},      primaryClass={cs.CV},      url={https://arxiv.org/abs/2303.05512}, }"
pretty_cite:
link: https://doi.org/10.48550/arXiv.2303.05512
topics: Physics, Simulation, System Identification, NeRF
reading_lists:
projects:
type:
to_read: false
stars:
---
**This one seems very relevant to Cyrus's problem**.
   Takes videos from many angles and determines physical properties of objects/its motion. NeRF: Neural Radiance Field. Takes many images, and generates a representation which can be used to create an image from any other angle. "Radiance Field" ascribes an emissivity and color to every point in space. This learns the volume shape.
   Continuum: continuous deformable medium. So goop/sand/playdoh. The parameters are learned. The NeRF model is also learned. Camera intrinsics/extrinsics are also measured. What is learned is the NeRF MLP parameters.

