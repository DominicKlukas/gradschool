---
tags:
  - technical_library
title: "Geometric Deep Learning: Grids, Groups, Graphs, Geodesics, and Gauges"
authors: Michael M. Bronstein, Joan Bruna, Taco Cohen, Petar Veličković
bibtex: "@misc{bronstein2021geometricdeeplearninggrids,      title={Geometric Deep Learning: Grids, Groups, Graphs, Geodesics, and Gauges},       author={Michael M. Bronstein and Joan Bruna and Taco Cohen and Petar Veličković},      year={2021},      eprint={2104.13478},      archivePrefix={arXiv},      primaryClass={cs.LG},      url={https://arxiv.org/abs/2104.13478}, }"
pretty_cite:
link: https://doi.org/10.48550/arXiv.2104.13478
topics: Equivariance, DL, CNNs
reading_lists: Foundational Textbooks
projects:
type:
to_read: true
stars:
---
Erlangen program showed that all of the fields of geometry that were being studied in the 19th century were similar in that they all assumed preservation under specific symmetries. In the same way that the field of geometry was fragmented during those days, so is deep learning right now. However, we can study in a similar way, that different architectures are designed for respecting the structure and symmetries of different domains.

# Introduction
Deep learning: (hierarchical) regularity and backprop are the key ingredients. By exposing the regularities, and exploiting them, we can overcome the curse of dimensionality. Showing how popular DL NN architectures exploit specific regularities in a systematic way, and the principles behind them, is the goal behind this paper.

# Learning in High Dimensions
- Classic DL fundamentals.
- Even if a set of functions is dense in the function space doesn't mean there is not inductive bias.
- Regularization means, out of the set of functions in your space that fit your dataset, you want the one that minimizes a complexity function, such as a norm, or the norm of the second derivative of the function, or the $L_{2}$ norm of the network weights.
Next, we think about how much data we would need in order to approximate a Lipschitz function... as we increase dimensions, the number of quadrants in which we need data to approximate the function increases exponentially. Lipschitz is a notion of regulary, and yet it still requires a ton of data!
If we have a fully connected neural network, which promotes sparse regularization (so most parameters are zero) then we are assuming many things, such as that the output function depends on low dimensional projects of the input, which is not the case if functions have long range correlations. (Long range correlations means that distance pixels have an effect on ones that are close by). We describe how this works in the next sections.
### TLDR
- Even if Lipschitz, dimension increase requires exponentially more data to approximate function.
- Even if we regulate with weights to, for example, enforce sparsity, this gives us unwanted biases.

# Geometric Priors
We will consider *signals* (functions) on some domain $\Omega$ (the signals are a vector space on this domain). We can define an inner product on the space.
Goemetric priors: translation symmetry, and scale separation.
Symmetry: transformation that leaves a certain property unchanged.

Next, we go through group theory fundamentals, definitions of equivariance and invariant functions, and group representations.

Image segmentation is when you assign to each pixel (or region an image) a classifier.