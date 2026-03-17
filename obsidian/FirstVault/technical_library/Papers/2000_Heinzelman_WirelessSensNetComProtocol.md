---
tags:
  - technical_library
title: Energy-efficient communication protocol for wireless microsensor networks
authors: W.R. Heinzelman; A. Chandrakasan; H. Balakrishnan
bibtex: "@INPROCEEDINGS{926982,  author={Heinzelman, W.R. and Chandrakasan, A. and Balakrishnan, H.},  booktitle={Proceedings of the 33rd Annual Hawaii International Conference on System Sciences},   title={Energy-efficient communication protocol for wireless microsensor networks},   year={2000},  volume={},  number={},  pages={10 pp. vol.2-},  keywords={Energy efficiency;Wireless application protocol;Wireless communication;Microsensors;Energy dissipation;Routing protocols;Telecommunication network reliability;Monitoring;Spread spectrum communication;Scalability},  doi={10.1109/HICSS.2000.926982}}"
pretty_cite:
link: https://ieeexplore.ieee.org/document/926982/authors#authors
topics: Sensor Networks
reading_lists: DL Project
projects: DL Project
type:
to_read: false
stars:
---
We have a network of sensors, which is large. Each sensor is inexpensive, and they are all identical. We model the amount of energy dissipated by the sensors in sending information through a first order radio model which is $O(d^{2}, k)$ in the distance $d$ to the receiver and $k$ the length of the signal, and $O(k)$ energy to receiver a message. Sensors always have data to send (so communicate consistently). "First node death" is the first instance when one of the many nodes runs out of battery.

Their solution has the following characteristics:
- randomly selecting a node in a cluster to be the "sender" at different points in time, in order to distribute the expense of sending the signal to the base station.
- Preprocessing information to compress the data being sent to the base station, further reducing cost.  They call this "data fusion".

# 3. Two baseline routing protocol analysese
We start by comparing two routing baselines: Direct Transmission, where very node sends data directly to the base station (and so no transmission receiving cost gets incurred) and Minimum Transmission Energy, where every node gets routed through intermediate nodes to minimize the transmission cost. DT favors nodes close to the base station, and MTE favors nodes far away (since the nodes close to the base station will have many nodes routed through it).
# 4. LEACH Low-Energy Adaptive Clustering Hierarchy
- Given a desired number of cluster head nodes, a node volunteers to be a cluster head such that probabilistically, the correct proportion of nodes will be cluster heads. It basically determines how long it has been since it has been a cluster head last.
- All the other nodes then listen to a homing signal sent by all the newly identified cluster nodes, and they choose to send their data to the closest cluster node (the one with the strongest signal).
- Periodically, these cluster-heads will get re-assigned.


