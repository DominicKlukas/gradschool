---
tags:
  - technical_library
title: "Visual Autoregressive Modeling: Scalable Image Generation via Next-Scale Prediction"
authors: Keyu Tian, Yi Jiang, Zehuan Yuan, Bingyue Peng, Liwei Wang
bibtex: "@misc{tian2024visualautoregressivemodelingscalable,      title={Visual Autoregressive Modeling: Scalable Image Generation via Next-Scale Prediction},       author={Keyu Tian and Yi Jiang and Zehuan Yuan and Bingyue Peng and Liwei Wang},      year={2024},      eprint={2404.02905},      archivePrefix={arXiv},      primaryClass={cs.CV},      url={https://arxiv.org/abs/2404.02905}, }"
pretty_cite:
link: https://doi.org/10.48550/arXiv.2404.02905
topics:
reading_lists:
projects:
type:
to_read: false
stars:
---
# First Reading
What type of paper: a new type of model. Look to understand how it works, and the previous architectures, what they didn't do well, and why this one works so much better.


# Terms
- Autoregression: when you factor a probability distribution as 
$$
p(x_{1}, x_{2}, \dots, x_{n}) = \prod_{k=1}^K p(x_{k} | x_{<k})
		$$
	Inference time, the distribution is sampled as: $x_{1} \sim p(x_{1}), x_{2} \sim p(x_{2} | x_{1}), \dots, x_{K} \sim \prod_{k=1}^K p(x_{k} | x_{<k})$.
- Raster-scan: moving on a screen left to right top to bottom. The old way images may have been generated.
- Zero shot: when you do something you weren't trained on without additional fine tuning. LLMs have this property: there are many separate tasks you can encode as text instructions, so if you learn an LLM you don't need extra training for each task.


# Questions
3.1 
- How does the tokenization work?
	- They design the tokens through autoencoders