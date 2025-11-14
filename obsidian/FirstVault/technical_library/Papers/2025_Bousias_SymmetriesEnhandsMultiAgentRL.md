---
tags:
  - technical_library
title: Symmetries-enhanced Multi-Agent Reinforcement Learning
authors: Nikolaos Bousias, Stefanos Pertigkiozoglou, Kostas Daniilidis, George Pappas
bibtex:
pretty_cite:
link:
topics: Equivariance, RL, Multi Agent
reading_lists:
projects:
type:
to_read: false
stars:
---
Extrinsic vs Intrinsic symmetries... what is the difference?

They say that intrinsic symmetries are not common in dynamical systems... what does this mean?
I am going to assume that they use the definition given by R. Walter's paper: Extrinsic equivariance is when the model symmetry transforms the input data to out-of-distribution data.

When you permute robots, for example, the robots themselves might be slightly different, which would break symmetry.
We start with a symmetric architecture, but then, we learn an embedding that lets us break symmetry, but in the embedded space we indeed have perfect symmetry.