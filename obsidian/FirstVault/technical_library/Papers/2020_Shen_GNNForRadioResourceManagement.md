---
tags:
  - technical_library
title: "Graph Neural Networks for Scalable Radio Resource Management: Architecture Design and Theoretical Analysis"
authors: Yifei Shen; Yuanming Shi; Jun Zhang; Khaled B. Letaief
bibtex: "@ARTICLE{9252917,  author={Shen, Yifei and Shi, Yuanming and Zhang, Jun and Letaief, Khaled B.},  journal={IEEE Journal on Selected Areas in Communications},   title={Graph Neural Networks for Scalable Radio Resource Management: Architecture Design and Theoretical Analysis},   year={2021},  volume={39},  number={1},  pages={101-115},  keywords={Wireless networks;Neural networks;Resource management;Optimization;Computer architecture;Array signal processing;Scalability;Radio resource management;wireless networks;graph neural networks;distributed algorithms;permutation equivariance},  doi={10.1109/JSAC.2020.3036965}}"
pretty_cite:
link: https://ieeexplore.ieee.org/document/9252917
topics: Sensor Networks, DL, GNN
reading_lists: DL Project
projects: DL Project
type:
to_read: false
stars:
---
Many problems in radio resource allocation are non-convex, and solutions scale poorly. DL has been used because it lets you generalize your solution method to a wide array of problems, without needing to worry about domain specific knowledge. You can either learn an analytical solution (which might be slow to compute), or incorporate NNs in specific part of your algorithms. Also, most people use MLPs and CNNs, which scale poorly in these cases because they don't have good inductive bias. In this paper, they apply MPGNNs to wireless networks when they are formulated as graphs.

Channel state information: what a device knows about the channel being used, and its properties.

Note: they determine an equivalence between MPGNNs and traditional optimization algorithms which allow them to apply analysis designed for traditional algorithms.

