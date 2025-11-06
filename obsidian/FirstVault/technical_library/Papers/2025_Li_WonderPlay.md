---
tags:
  - technical_library
title: "WonderPlay: Dynamic 3D Scene Generation from a Single Image and Actions"
authors: Zizhang Li, Hong-Xing Yu, Wei Liu, Yin Yang, Charles Herrmann, Gordon Wetzstein, Jiajun Wu
bibtex: "@misc{li2025wonderplaydynamic3dscene,      title={WonderPlay: Dynamic 3D Scene Generation from a Single Image and Actions},       author={Zizhang Li and Hong-Xing Yu and Wei Liu and Yin Yang and Charles Herrmann and Gordon Wetzstein and Jiajun Wu},      year={2025},      eprint={2505.18151},      archivePrefix={arXiv},      primaryClass={cs.GR},      url={https://arxiv.org/abs/2505.18151}, }"
pretty_cite:
link: https://doi.org/10.48550/arXiv.2505.18151
topics: Generative AI, System ID, Physics Simulation
reading_lists:
projects:
type:
to_read: false
stars:
---
Learns possible implied shapes from data, so that it only requires 1 image to infer what a shape could be. Layers images into foreground (what can explicitly be seen by a camera), background (what is hidden, but still need structure) and sky (things in the image that don't have to be reconstructed). Uses a course physics solver (to add velocity, displacement to certain particles) but far from a comprehensive solution. Then, it applies a video generator with these updated positions as a bit of a seed, to add more realism from a video perspective to the surfel's positions. The frame is rendered from these surfels (mathematically), and then the next frame is computed. FLAGS and video generator are learned.