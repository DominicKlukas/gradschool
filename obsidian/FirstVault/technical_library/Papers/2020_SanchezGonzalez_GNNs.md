---
tags:
  - technical_library
title: Learning to Simulate Complex Physics with Graph Networks
authors: Alvaro Sanchez-Gonzalez, Jonathan Godwin, Tobias Pfaff, Rex Ying, Jure Leskovec, Peter W. Battaglia
bibtex: "@misc{sanchezgonzalez2020learningsimulatecomplexphysics,      title={Learning to Simulate Complex Physics with Graph Networks},       author={Alvaro Sanchez-Gonzalez and Jonathan Godwin and Tobias Pfaff and Rex Ying and Jure Leskovec and Peter W. Battaglia},      year={2020},      eprint={2002.09405},      archivePrefix={arXiv},      primaryClass={cs.LG},      url={https://arxiv.org/abs/2002.09405}, }"
pretty_cite:
link: https://doi.org/10.48550/arXiv.2002.09405
topics: Physics, Deep Learning, GNN
reading_lists:
projects:
type:
to_read: true
stars:
---
You have an encoder, which converts your system and its dynamics into a graph. There is then a "message passing" function which is learned, that determines the interactions between the nodes, which are then propagated over a series of steps (so that a force from a source node propagates to nodes a distance n away from it after the n-th step). Then, a decoder converts the graph back into the particle system, and then integrates to get the resulting particle states. Computes the predicted accelerations at each step and compares to ground truth (at each step).