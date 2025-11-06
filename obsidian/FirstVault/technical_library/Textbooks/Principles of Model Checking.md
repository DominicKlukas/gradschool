---
tags:
  - technical_library
title: Principles of Model Checking
authors: Christel Baier, Joost-Pieter Katoen
bibtex:
pretty_cite:
link:
topics:
reading_lists: Safe RL
projects:
type:
to_read: true
stars:
---
I read some bits on NFAs... nondeterministic finite automaton. Basic, intuitive definition. Describes a system that recieves commands which result it going from one state to the next, where these states are subsets of some set of states. They are finite because the words they recieve (each letter is a command) are finitely long. This is different from Buechi automata: they can have infinitely long commands.

Temporal logic: New symbols! Triangle: something will eventually happen. Square: something is happening now and always will. Circle: something will happen next step. U: Something is true until something else will happen. Time stamps are discrete.

Linear temporal logic analyzes sequences, and what can be said about the states in the sequences. Computational tree logic analyzes trees.