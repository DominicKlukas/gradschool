---
tags:
  - technical_library
title: "PDE-Transformer: Efficient and Versatile Transformers for Physics Simulations"
authors: Benjamin Holzschuh, Qiang Liu, Georg Kohl, Nils Thuerey
bibtex: "@misc{holzschuh2025pdetransformerefficientversatiletransformers,      title={PDE-Transformer: Efficient and Versatile Transformers for Physics Simulations},       author={Benjamin Holzschuh and Qiang Liu and Georg Kohl and Nils Thuerey},      year={2025},      eprint={2505.24717},      archivePrefix={arXiv},      primaryClass={cs.LG},      url={https://arxiv.org/abs/2505.24717}, }"
pretty_cite:
link: https://doi.org/10.48550/arXiv.2505.24717
topics:
reading_lists:
projects:
type:
to_read: false
stars:
---
Applies transformer architecture to PDE problem, by tokenizing partitions of the entire space and for each token predicting the next time point for a certain PDE. All the weights inside the transformer are a function of metadata, so that many PDEs can be solved by the same transformer. The transformer also has a U like structure, where after tokens go through one layer, the next layer has the same token size but fewer tokens, with each token representing a bigger partition of the grid.