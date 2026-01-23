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
If we have a fully connected neural network, which promotes sparse regularization (so most parameters are zero) then we are assuming many things, such as that the output function depends on low dimensional projections of the input, which is not the case if functions have long range correlations. (Long range correlations means that distant pixels have an effect on ones that are close by). We describe how this works in the next sections.
### TLDR
- Even if Lipschitz, dimension increase requires exponentially more data to approximate function.
- Even if we regulate with weights to, for example, enforce sparsity, this gives us unwanted biases.

# Geometric Priors
We will consider *signals* (functions) on some domain $\Omega$ (the signals are a vector space on this domain). We can define an inner product on the space.
Goemetric priors: translation symmetry, and scale separation.
Symmetry: transformation that leaves a certain property unchanged.

What is scale separation?

Next, we go through group theory fundamentals, definitions of equivariance and invariant functions, and group representations.

Image segmentation is when you assign to each pixel (or region an image) a classifier. We would expect segmentation functions to be equivariant to translation.
We look at different types of automorphisms/isomorphisms that apply to the whole domain.

For the next three sections, we are interested in creating a function which is invariant to group transformations of an underlying domain, and robust to transformations that are similar but not exactly the same as the group transformations (stability).
### 3.3 Deformation Stability
- Groups describe transformations of the entire domain (like rotations of a whole image), but they do not show local symmetries well (if only one part of the image translates but the whole image doesn't). Then, we have states that might be semantically related (so we wanted them to be related by the symmetry) but not globally by our coarse symmetry.
- If a 3D object is deformable, it may be hard to describe the transformations which preserve the object's identity.
- Geometrically stable function: when the domain is transformed by automorphisms $\tau$ which are "close enough" to group transformations, where "close enough" is specified by some function $c(\tau)$, (like such local symmetric transformations) and we have some function $f$ of the data, deformation stability will be defined by the expression $$
\lvert f(\rho (\tau x)) - f(x) \rvert \leq C c(\tau) \lvert x \rvert , \forall x \in \mathcal{X}
$$
- An example of such a function $c$ might be $\int_{\Omega} \lvert \nabla \tau (u) \rvert du$, which measures how much $\tau$ differs from a translation.
- Sometimes the domain itself changes, for example if the domain is a manifold or a graph. In that case, we can consider how different a distorted domain is from the original one, by finding an isomorphism between the two which changes the structure as little as possible. The distance between two manifolds/graphs might be $$
d_{\mathcal{D}}(\Omega, \tilde{\Omega}) = \text{inf}_{\eta \in \mathfrak{G}} \lvert d - \tilde{d} \cdot (\eta \times \eta) \rvert 
$$
- Here, we take two elements from $\Omega$, put them through the isomorphism into the $\tilde{\Omega}$ space, and compare distances.
- Finally, we can then see how stable a function is to variations in domain $$
\lvert f(x, \Omega) - f(\tilde{x}, \tilde{\Omega}) \rvert \leq C \lvert x \rvert d_{\mathcal{D}} (\Omega, \tilde{\Omega}).
$$
### 3.4 Scale Separation
- We can take fourier or wavelet decompositions of signals... both involve dot product with some kernel which reveals smootheness and scale regularities.
- Example: the shift operation is simply a diagonal operation in the fourier operation (independent of frequency), and is just an appropriate phase shift for each frequency. But if we have an approximate translation, then the errors can be very big, not scaling down once the approximate translation becomes smaller. We don't have this problem with wavelets, and so wavelets are stable representations 
- Wavelets are useful, because they only analyze frequency data locally, not affecting the global coefficients just because of a small number of anomalies. (Piecewise smooth will have smooth coefficients in most places).
- Scale separation conceptually: data for different scales is separated out. That is, a function $f$ can be approximated as $f \approx f_{j} \cdot P_{j}$ where $P_{j}$ is a non-linear coarse graining (so not necessarily just an average) (that is, it takes local points and lumps them together somehow by analyzing/recognizing features). Then, we say a function is locally stable.

### 3.5 General Geometric DL Blueprint
- First, we recognize that if we want a group invariant function, if we restrict it to be a linear function, we have
- $$
f(x) = f(g\cdot x) \implies f(x) = \frac{1}{|G|} \int_{G} f(g\cdot x) = f\left( \frac{1}{|G|} \int_{G} g \cdot x \right)
$$
- where the last equality follows by linearity. For translation, for example, this only describes the average colour! But we might want translation invariant recognition of dogs or cats, so this definitely is not a vibe.
- Instead, we first compose equivariant functions with non-linear activation functions locally, for a few layers, until we have a final layer which is invariant. We can show by universal approximation theorems that this can then approximate any group invariant function.
- Finally, Fourier Transform vs Wavelet Transform showed us how it's bad when global interactions happen at a small scare for stability... even though we have global equivariance, we want high resolution equivariant maps to be "localized", depending on a receptive field (set of points close to a given point in our domain) leaving long scale interactions to deeper layers of the network.

# 4 
Here, we look at 5 examples of mathematical structures, which, when present on data which axiomatically describe function classes that can be used in our Geometric Deep Learning blueprint.
## 4.1 Graph Theory
A set is a graph with no edges. We describe sets with lists in computers; to achieve permutation invariance, we need to have invariance w.r.t. permutations (or equivariance) and we determine the form of the linear maps that would be required for each of these cases. (We did this in the DL class).
We proceed in the case with edges, were $F(PX, PAP^{\top}) = F(X, A)$.
Linear maps with this form have 1 of 15 forms (up to isomorphism?) which then generate the entire linear map, regardless of the dimension of the graph.
The non-linear maps we apply to nodes (and their neighborhoods) must be invariant to permutation as well, dependent on the features of the node and the features of the node's neighbors.
Pooling operations can also be more complicated.
## 4.2 Grids
Convolution iff translation equivariant.
In linear algebra, a set of linear operators is jointly diagonalizable iff they mutually commute (so they share eigenvectors).
This turns out to be the discrete Fourier basis! So, we can take the fourier transform, (We can do the n^2 computation with the basis vectors, or we can do the FFT which recognizes all the doubled up multiplication redundancies).
Then, any convolution will be a diagonal matrix w.r.t. this basis, and after that we turn back into the original basis.

Laplacian is translation invariant, and interesting, because it captures deep geometric information. At each value it describes how much that value changes w.r.t. the neighbors around it in a special way. It's eigenvectors are the Fourier basis for a grid, so we can also take it for a graph after having fixed a basis (node ordering), although as an operator it is independent of this.

## 5.2 Graph Neural Networks
In the most general case, we have the following form for GNNs: 
$$
h_{u} = \phi \left( x_{u}, \bigoplus_{v \in \mathcal{N}(u)} \varphi(x_{v}, x_{u}) \right)
$$
Here, $\varphi$ is either an attention mechanism, not dependent on $x_{u}$, or a more general, learned function. Since the same function $\varphi$ is being applied to each neighbor, and the same function $\phi$ is being applied to each node $u$, we have that this is permutation equivariant.