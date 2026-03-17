---
tags:
  - technical_library
title: "HGNN: A Hierarchical Graph Neural Network Architecture for Joint Resource Management in Dynamic Wireless Sensor Networks"
authors: Le Tung Giang; Nguyen Xuan Tung; Vu Hoang Viet; Trinh Van Chien; Nguyen Tien Hoa; Won Joo Hwang
bibtex: "@ARTICLE{10738316,  author={Giang, Le Tung and Tung, Nguyen Xuan and Viet, Vu Hoang and Chien, Trinh Van and Hoa, Nguyen Tien and Hwang, Won Joo},  journal={IEEE Sensors Journal},   title={HGNN: A Hierarchical Graph Neural Network Architecture for Joint Resource Management in Dynamic Wireless Sensor Networks},   year={2024},  volume={24},  number={24},  pages={42352-42364},  keywords={Wireless sensor networks;Sensors;Resource management;Throughput;Servers;Power demand;Graph neural networks;Wireless communication;Quality of service;Internet of Things;Access point (AP) selection;hierarchical graph neural networks (HGNNs);hierarchical wireless sensor network (HWSNs);Internet-of-Things (IoT) sensor networks;power allocation},  doi={10.1109/JSEN.2024.3485058}}"
pretty_cite:
link: https://ieeexplore.ieee.org/document/10738316
topics: Sensor Networks, DL, GNN
reading_lists:
projects:
type:
to_read: false
stars:
---
Terms
- Heuristic Approaches: practical rule, not guaranteed to be optimal, computationally cheap, and works in practice.

Abstract
- Wireless Sensor Networks (WSN) need to be managed well to save energy
- Traditional algorithms scale poorly.
- GNNs scale well, but don't perform well when they fail to capture hierarchy.
- HGNNs deal with different levels effectively.
Introduction
- WSNs are powerful, with all these new technologies and applications
- Energy usage remains a big problem, while still ensuring quality of transmissions.
- Resource Management is an NP-hard problem.
- Dynamic WSNs: batteries drain, throughput requirements change, etc. This has not been researched well enough yet.
- Literature Review
	- Hierarchical structures have been considers.
	- GNNs have been considered (handle the graph-nature of the data well)
	- GNNs are flat... they always only consider next edge, regardless of how big the graph is, so they don't do a good job with hierarchical thinking.
	- GNNs don't consider edges, only nodes. This is a problem, when we have interference denoted by edges.
System Model
- Set of sensors, set of access nodes which send info to the server.
- Two stages: sensors talk to AP, AP talks to server
- Sensors interfere, reduce their quality. Power level of each sensor has to be determined.
- We have a data throughput rate, determined by the interference (fancy communications physics equations).


They apply a simple GNN scheme (twice) once to the SN->AP graph and then once on the AP -> Server graph, and then show that they take names on the thing that they did.