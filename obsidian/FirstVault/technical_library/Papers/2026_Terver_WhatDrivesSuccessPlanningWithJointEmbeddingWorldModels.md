---
tags:
  - technical_library
title: What Drives Success in Physical Planning with Joint-Embedding Predictive World Models?
authors: Basile Terver, Tsung-Yen Yang, Jean Ponce, Adrien Bardes, Yann LeCun
bibtex: |-
  @misc{terver2026drivessuccessphysicalplanning,
        title={What Drives Success in Physical Planning with Joint-Embedding Predictive World Models?}, 
        author={Basile Terver and Tsung-Yen Yang and Jean Ponce and Adrien Bardes and Yann LeCun},
        year={2026},
        eprint={2512.24497},
        archivePrefix={arXiv},
        primaryClass={cs.AI},
        url={https://arxiv.org/abs/2512.24497}, 
  }
pretty_cite:
link: https://arxiv.org/abs/2512.24497
topics: World Models, Planning, Joint-Embedding
reading_lists:
projects:
type:
to_read: false
stars:
---
Learning Goals
- What is the state of the performance of these models?
- What makes them succeed?

They do well on tasks with sparse rewards, compared to RL, and they do better than other JEPA world models on the tasks they chose.

What made them succeed?
- Train latent dynamics with multi-step roll outs, rather than just teacher forcing. Latent dynamics is the bottleneck.
- You need a bigger input window in order to see velocity/acceleration.
- Proprioception in your latent space is helpful.
- In your planning algorithm, don't use gradient based method, use a sampling based method.