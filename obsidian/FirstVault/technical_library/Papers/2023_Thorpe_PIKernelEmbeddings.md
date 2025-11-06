---
tags:
  - technical_library
title: "Physics-Informed Kernel Embeddings: Integrating Prior System Knowledge with Data-Driven Control"
authors: Adam J. Thorpe, Cyrus Neary, Franck Djeumou, Meeko M. K. Oishi, Ufuk Topcu
bibtex: "@misc{thorpe2023physicsinformedkernelembeddingsintegrating,      title={Physics-Informed Kernel Embeddings: Integrating Prior System Knowledge with Data-Driven Control},       author={Adam J. Thorpe and Cyrus Neary and Franck Djeumou and Meeko M. K. Oishi and Ufuk Topcu},      year={2023},      eprint={2301.03565},      archivePrefix={arXiv},      primaryClass={eess.SY},      url={https://arxiv.org/abs/2301.03565}, }"
pretty_cite:
link: https://doi.org/10.48550/arXiv.2301.03565
topics: Physics, Dynamics, Kernel Embeddings
reading_lists:
projects:
type:
to_read: false
stars:
---
## Understanding Kernel Distribution Embeddings
We have a set of (typically Gaussian) basis functions. We want to compute $Q( \cdot | x ,u)$, which assigns a probability measure of the state space to every state and action. (If I am in state x and do u, what state $x_{t + 1}$ will I end up in, with what distribution?) The nice thing about probability distributions, is that it is very easy to compute something called a kernel embedding, which is a function $m(u, x)$ such that $\langle f, m \rangle  = E_{Q(\cdot | x, u)} [ f(x, u)]$. Consider a finite probability distribution to understand how this works: If state $x_i$ happens with probability $1/n$, then $m$ is defined as $\frac{1}{n} \sum_i k(\cdot, x_i)$, and when you take the dot product with some $f$, the way that kernel functions work is that $\langle f, k(\cdot, x_i) \rangle = f(x_i)$ so we can see that this will give use $E[f(x)] = \sum \frac{1}{n} f(x_i)$ as desired. In general, don't expect the coefficients (or the integral over the coefficients) of the k's to sum to 1, since we only need the expectation value when we take the dot product with f to be an expectation value: this is the requirement, not that the coefficients sum to 1.

Next, the data driven approach is then to compute this m with

$$\hat{m} = \arg \min_{f \in \mathcal{V}} \frac{1}{2\lambda} \sum_{i = 1}^M || k(y_i, \cdot) - f(x_i, u_i) ||^2_{\mathscr{H}} + \frac{1}{2}||f||^2_{\mathcal{V}}$$
To understand this, consider computing this at a single input, to try and get the probability distribution. Then, after taking the derivative to get the minimum, we would see that once it is equal to zero, we would get $M \cdot f = \sum_i^M k(y_i)$, or in other words $f = \frac{1}{M} \sum_i^M k(y_i)$, which is precisely the mean of these kernel functions, which gives us a function where when we take the dot of $\langle c, f \rangle$ then we get the desired expectation.

That's the machinery and understanding behind kernel functions! They can be used to create useful approximates for functions, especially in this probability distribution context.

Cyrus's paper (this paper) adds a physics loss term to help us learn f more quickly/accurately.

