---
tags:
  - technical_library
title: Exploiting Approximate Symmetry for Efficient Multi-Agent Reinforcement Learning
authors: Batuhan Yardim, Niao He
bibtex: "@misc{yardim2024exploitingapproximatesymmetryefficient,      title={Exploiting Approximate Symmetry for Efficient Multi-Agent Reinforcement Learning},       author={Batuhan Yardim and Niao He},      year={2024},      eprint={2408.15173},      archivePrefix={arXiv},      primaryClass={cs.GT},      url={https://arxiv.org/abs/2408.15173}, }"
pretty_cite:
link: https://doi.org/10.48550/arXiv.2408.15173
topics: Equivariance, RL, Multi Agent
reading_lists:
projects:
type:
to_read: false
stars:
---
MARL problems have the "curse-of-many-agents" which makes it intractable. Researchers search for "islands of tractability".
Symmetry: when all agents have the same reward function and dynamics.
This is a theoretical paper. It basically says, that even if the dynamics of mean field games (which do analysis on games with infinitely many agents in the limit, that are perfectly symmetrical) are not perfectly symmetrical, we can bound the breaking of the symmetry (how different different players are from each other) and then still do some similar analysis that we would for perfectly symmetrical games.
$\alpha$ says how different the dynamics are, $\beta$ says how different the rewards are, and then the approximate Nash equilibrium is similar.
Nash equilibrium: no player can improve their own outcome by changing their strategy.