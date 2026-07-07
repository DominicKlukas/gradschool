---
tags:
  - technical_library
title: Reward Machines for Cooperative Multi-Agent Reinforcement Learning
authors: Cyrus Neary, Zhe Xu, Bo Wu, Ufuk Topcu
bibtex:
pretty_cite:
link: https://arxiv.org/abs/2007.01962
topics: MARL, Automata Theory, Reward Machines, Mealy Machines
reading_lists:
projects: MARL Project
type:
to_read: false
stars:
---
We have a standard MARL environment, where the local state spaces of each individual agent are concatenated in a product space to make the state space of the entire team. The reward machine is a formalism for a flowchart that describes the high level task. A labeling function maps an ordered pair consisting of the RM and MDP state space to an event (which then advances the RM). The paper shows that we can decompose an RM into a "projected" RM for each individual agent, by considered the set of RM states/events which are relevant to each agent, where agents that share events that are relevant to each both agents "synchronized" in the sense that they only progress their individual RMs using an event once all of the agents agree that the event has occurred.
The main theorems show that the decomposed RM and the original RM are equivalent, and likewise, with their definition of the decomposed labeling function it works equivalently to the original team wise labeling function with synchronization.
One important detail: when training agents individually, other agents performance on synchronized tasks are simulated by randomizing the amount of time before the other agents consider their contribution to the event to be "done" on a shared event.