---
tags:
  - technical_library
title: "Theoretical Foundations of Representation Learning using Unlabeled Data: Statistics and Optimization"
authors: Pascal Esser, Maximilian Fleissner, Debarghya Ghoshdastidar
bibtex: "@misc{esser2025theoreticalfoundationsrepresentationlearning,      title={Theoretical Foundations of Representation Learning using Unlabeled Data: Statistics and Optimization},       author={Pascal Esser and Maximilian Fleissner and Debarghya Ghoshdastidar},      year={2025},      eprint={2509.18997},      archivePrefix={arXiv},      primaryClass={cs.LG},      url={https://arxiv.org/abs/2509.18997}, }"
pretty_cite:
link: https://doi.org/10.48550/arXiv.2509.18997
topics: DL, Representation Learning
reading_lists:
projects:
type:
to_read: false
stars:
---
Mathematical tools from stats and optimization aim to explain why new principles in unsupervised representation learning work so well, though this is a hard task. This paper gives an overview of recent theoretical advances in this direction.

Euclidean representations: they have nice norm properties, which allow us to compare data by distance.
Data compression representations: are more compressed (less data for a given representation) but might not have these nice norm properties.

Modern Rep. learning is focused on visual and text data because of VLMs and LLMs. It often uses deep learning on unlabelled data.
A word on deep learning:
- Standardized implementation method: same optimisers on new loss functions and new architectures + huge computing power makes it really convenient.
- Scaling laws, which guide design, are empirical and so not really watertight
- Lack of understanding of the representations, confusion in fact
	- Classical learning theory says that you need a simple model (give me 4 parameters and I can fit an elephant... 5 and I can make his )