---
tags:
  - technical_library
title: Policy Gradient Methods in the Presence of Symmetries and State Abstractions
authors: Prakash Panangaden, Sahand Rezaei-Shoshtari, Rosie Zhao, David Meger, Doina Precup
bibtex: "@misc{panangaden2024policygradientmethodspresence,      title={Policy Gradient Methods in the Presence of Symmetries and State Abstractions},       author={Prakash Panangaden and Sahand Rezaei-Shoshtari and Rosie Zhao and David Meger and Doina Precup},      year={2024},      eprint={2305.05666},      archivePrefix={arXiv},      primaryClass={cs.LG},      url={https://arxiv.org/abs/2305.05666}, }"
pretty_cite:
link: https://doi.org/10.48550/arXiv.2305.05666
topics: RL, State Abstractions, MDP Homomorphisms, Representation Learning
reading_lists:
projects: Equivariance Gain Predictor
type:
to_read: false
stars:
---
They formalize MDP homomorphisms in the case of continuous functions, and then show how we can learn MDP homomorphisms in the case of continuous state-action spaces that are true structure preserving homomorphisms.

The Homomorphic Policy Gradient allows one to compute policy updates in a compressed, abstract MDP—obtained via a learned homomorphism—while still improving performance in the original environment. When parameters are shared, the abstract gradient becomes an alternative, potentially lower-variance estimate of the true policy gradient.

Main takeaways from the way they learn their homomorphisms:
- You have to couple this homomorphism to policy learning. That way, the relevant state spaces are learned.
- Use bi-simulation metrics to group states together (if their bi-simulation metric is small).