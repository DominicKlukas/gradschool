---
tags:
  - technical_library
title: "Flow Equivariant World Models: Memory for Partially Observed Dynamic Environments"
authors: Hansen Jin Lillemark, Benhao Huang, Fangneng Zhan, Yilun Du, Thomas Anderson Keller
bibtex: |-
  @misc{lillemark2026flowequivariantworldmodels,
        title={Flow Equivariant World Models: Memory for Partially Observed Dynamic Environments}, 
        author={Hansen Jin Lillemark and Benhao Huang and Fangneng Zhan and Yilun Du and Thomas Anderson Keller},
        year={2026},
        eprint={2601.01075},
        archivePrefix={arXiv},
        primaryClass={cs.LG},
        url={https://arxiv.org/abs/2601.01075}, 
  }
pretty_cite:
link: https://arxiv.org/abs/2601.01075
topics: Equivariance, World Models
reading_lists:
projects:
type:
to_read: false
stars:
---
Learning Goals
What is the problem they are trying to solve?
In what way is equivariance being used in this paper?
In what sense do they understand the world "flow"?

## Problem statement
World models work well, but with partially observed environments, there are issues (point will be made).
- They use transformers on video data
- Your attention window is limited (video is expensive to take attention over)
- So, past information about a scene you have turned away from will eventually be lost.
- Even if you keep past information, it might not be helpful in a dynamic situation.
- They solve this problem!

They do so by learning 