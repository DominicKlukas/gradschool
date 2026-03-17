---
tags:
  - technical_library
title: E(n) Equivariant Graph Neural Networks
authors: Victor Garcia Satorras, Emiel Hoogeboom, Max Welling
bibtex: "@misc{satorras2022enequivariantgraphneural,      title={E(n) Equivariant Graph Neural Networks},       author={Victor Garcia Satorras and Emiel Hoogeboom and Max Welling},      year={2022},      eprint={2102.09844},      archivePrefix={arXiv},      primaryClass={cs.LG},      url={https://arxiv.org/abs/2102.09844}, }"
pretty_cite:
link: https://doi.org/10.48550/arXiv.2102.09844
topics: Equivariance, DL, Graphs, Dynamical Systems
reading_lists:
projects:
type:
to_read: false
stars:
---
They develop a new architecture for graph neural networks.
They make the networks equivariant by doing message passing (computing a quantity $m_{ij}$ for the relationship between each of the two connected nodes and summing over them to make it permutation invariant, it is E2 equivariant by the nature of the way they compute the functions).
Invariant w.r.t. rotations, equivariant w.r.t. reflections, translations, and rotations.
We use MLPs to compute the message passing functions.
Other innovation: we can learn what edges are there using a soft-max function if necessary (there aren't too many nodes to have a fully connected graph be infeasible). Otherwise, could be computed by proximity (kNN).

Summary: I have a good understanding of the architecture.
Presentation flow:
- Introduce the type of problem you would want to apply this to.
- Introduce how these networks work.
- Introduce the results.

- For problem setup and motivation, we should probably remind them of the problem class, and the idea of equivariance (which they know already). We can also identify the gap: previous equivariance models were complicated, and didn't scale to higher dimensions.
- The contributions are not very complicated. They essentially message pass the euclidean distance between nodes along with other scalar features as scalar parameters to the message passing, while doing a vector update based on the unit vector going from one node to the other, while scaling this vector by another SE(N) invariant message passing function. I suggest we go into detail here since there is not so much detail we need to cover. We can do the equivariance proofs in the appendex without any issues I suppose.
- For two of the experiments (dynamical systems and molecule property estimator), they compare with the architectures we have been looking at in the past weeks. We should definitely mention these when we look at the experimental results, and also compare to the results they give to make sure it is consistent.
- Take home messages: make it clear that this model is not as expressive as TFNs or SE3 transformers, and discuss why this does or doesn't matter. Also, discuss where in the literature this model fits (briefly review relevant aspects of TFNs and SE3 transformer, and how this is different). Research, and make clear the problem most GNNs have, that they struggle to learn overarching long range structure (and often just become local averaging machines), and also talk about ways this can be mitigated/improved, (to be a suggestion about how this work can be improved) or perhaps do a literature search to see where this architecture was taken further in the papers that came after it.

- As for how we break it up, I would suggest one person does the technical contributions, another does the empirical contributions, and finally the last person does the take home messages/additional comments. I wouldn't mind doing take home messages, since I have read lots of equivariance papers and would be excited to talk about surrounding literature/significance of this paper specifically. I can also do problem setup and motivation, since it is a tune all of us have heard many times before (very similar scope to the papers other students have read just now) so is really not a lot of work. But I'm ok with anything

Introduce the problem, in the context of the algorithms we have seen so far.
Say
- In the past few weeks, we have looked at a slew of different algorithms related to equivariance.
- We have learned how graph neural networks work. Group equivariant CNNs. Tensor field networks.
The whole principle behind these networks is, that when our data has underlying symmetries, these networks provide helpful inductive biases that then enable much greater generalization and therefore sample efficiency.


Take home messages
- Writing is ok
- E(n) is nonsense
- Important things learned
	- A bunch of these architectures, including ones we have seen in previous weeks, can be consolidated as GNNs with different message passing equations
- Raise questions we have
	- E(n) - this is a big one. When is the euclidean group of order n actually a useful inductive bias, aside from the cases 1, 2, and 3
- How do we deal with long range relationships
	- Transformers are: easy to compute, since parallelizable. Use them somehow to get the long range information.
	- Practical solution: use two level graphs if you are able to, for specific problems.
	- Graph Laplacian (We would need to know how this works)