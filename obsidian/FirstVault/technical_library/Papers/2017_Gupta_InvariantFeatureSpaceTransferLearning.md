---
tags:
  - technical_library
title: Learning Invariant Feature Spaces to Transfer Skills with Reinforcement Learning
authors: Abhishek Gupta, Coline Devin, YuXuan Liu, Pieter Abbeel, Sergey Levine
bibtex: "@article{DBLP:journals/corr/GuptaDLAL17,  author       = {Abhishek Gupta and                  Coline Devin and                  Yuxuan Liu and                  Pieter Abbeel and                  Sergey Levine},  title        = {Learning Invariant Feature Spaces to Transfer Skills with Reinforcement                  Learning},  journal      = {CoRR},  volume       = {abs/1703.02949},  year         = {2017},  url          = {http://arxiv.org/abs/1703.02949},  eprinttype    = {arXiv},  eprint       = {1703.02949},  timestamp    = {Thu, 30 Jul 2020 17:47:49 +0200},  biburl       = {https://dblp.org/rec/journals/corr/GuptaDLAL17.bib},  bibsource    = {dblp computer science bibliography, https://dblp.org}}"
pretty_cite:
link: https://doi.org/10.48550/arXiv.1703.02949
topics: Transfer Learning, Reinforcement Learning, Invariant Feature Space
reading_lists:
projects:
type:
to_read: false
stars:
---

We have two different MDPs for two different robots. But we learn a function that maps the states of both of the spaces to a new space, such that similar states are mapped together. We do so by training two "autoencoders" $f$ and $g$ and then training a loss function that minimizes the distance between the two.