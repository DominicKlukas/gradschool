---
tags:
  - technical_library
title: Learning Latent Dynamics for Planning from Pixels
authors: Danijar Hafner, Timothy Lillicrap, Ian Fischer, Ruben Villegas, David Ha, Honglak Lee, James Davidson
bibtex: "@article{DBLP:journals/corr/abs-1811-04551,  author       = {Danijar Hafner and                  Timothy P. Lillicrap and                  Ian Fischer and                  Ruben Villegas and                  David Ha and                  Honglak Lee and                  James Davidson},  title        = {Learning Latent Dynamics for Planning from Pixels},  journal      = {CoRR},  volume       = {abs/1811.04551},  year         = {2018},  url          = {http://arxiv.org/abs/1811.04551},  eprinttype    = {arXiv},  eprint       = {1811.04551},  timestamp    = {Fri, 23 Nov 2018 12:43:51 +0100},  biburl       = {https://dblp.org/rec/journals/corr/abs-1811-04551.bib},  bibsource    = {dblp computer science bibliography, https://dblp.org}}"
pretty_cite:
link: https://doi.org/10.48550/arXiv.1811.04551
topics: Planning, Latent Dynamics
reading_lists:
projects:
type:
to_read: false
stars:
---
## Introduction
Planning!
Benefits
- Dynamics lets us plan in unknown environments
- Richness of a training singal: you learn much more from your data (how to plan, your latent space, and how much it matches) than you would if you were just learning sparse rewards
- No Bellman backups, and increased performance by increasing computational budget
Drawbacks
- Typically cannot envision multiple futures
- Overconfidence outside training distribution.
## Latent Space Planning
Lots of concepts here that I need to learn... VAEs, etc.
Something about learning a posterior distribution, and a probability over latent states? instead of a deterministic state (which is the difference between AEs and VAEs?)