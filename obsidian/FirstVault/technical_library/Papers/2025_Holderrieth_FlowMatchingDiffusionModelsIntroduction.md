---
tags:
  - technical_library
title: An Introduction to Flow Matching and Diffusion Models
authors: Peter Holderrieth, Ezra Erives
bibtex:
pretty_cite:
link: https://doi.org/10.48550/arXiv.2506.02070
topics: Flow Matching, Diffusion Models, Generative AI
reading_lists: Foundational Textbooks
projects:
type:
to_read: true
stars:
---
Teaches the math and concepts behind generative AI models

## Introduction
### Overview
SOTA Generative AI uses two concepts: flow matching and diffusion models to convert noise into data. ODEs and SDEs form the backbone. DNNs train the O/SDEs

### Modalities and Data
Modalities are not just datatypes: they traditionally describe the nature of the source of the information, such as audio, visual, etc.
When we represent data of different modalities as datatypes, we can flatten it into a vector in $\mathbb{R}^d$, in all of the applications used in this text.

### Generation
We consider the set of all possible outputs e.g. images. We put a probability distribution over the outputs, and then assign a measure based on how likely it is that that image satisfies the favorable criteria that we want for an image to be deemed "a success".
Generation, is then sampling this probability distribution.
Before such a generation model can be created, we need data. A dataset consists of finitely many data points sampled from the true distribution, which we then use to re-create the underlying probability distribution.
Conditional generation is when you add a condition to your distribution (to get another probability distribution). In this case, during training our dataset gives us access to pairs, $(z_i, y)$, where $z_i$ is the data, and $y$ is the condition. and  ==but I assume in some clever way you are making use of the distribution you already have? Q!==
Yes. This is precisely what chapter 5 is all about!

## Flow models
Flow, is another way of thinking about the solution of an ODE. Normally, you start at $x_0 \in \mathbb{R}^d$, and you are interested in a solution $x(t)$, which sees how the position evolves in $\mathbb{R}^d$ as we progress through time. However, flow rather fixes a time and has interest in how our position at a given point in time would change if we started at a different initial condition. A diffeomorphism is a continuously differentiable function with a continuously differentiable inverse.
Flow models work by taking the initial $x_0$ sampled from an initial distribution, and parameterizing an ODE vector field function $u_{t}^{\theta}(X_t)$ which then propagates these initial points such that if we sample where they end up, we would get a distribution that matches the distribution generating the data, $p_{data}$.
In order to sample this distribution, we would sample $p_{init}$, and then propagate it until the ending time (in this text, $t=1$) until we are at the data distribution.
This is a flow model.

## Diffusion Models
A stochastic process is a trajectory which is a random variable at every point in time.
One way we can do this is by adding Brownian motion to our ODE.
Has a few defining properties
- $W_t - W_s \sim \mathcal{N}(0, (t-s)I_d)$ for $0 \leq s \leq t$
- Increments are independent random variables.
Nowhere differentiable, and continuous.
We write an SDE as:
$$X_{t+1} = X_t + h u_t(X_t) + \sigma_t (W_{t+h} - W_t) + h R_t (h) $$
Here $\sigma_t$ is a function of time, or sometimes, a function of the state as well, but it is not a function of the Brownian motion.
The solution is unique, in the sense that there is a stochastic process which matches the distribution almost surely.
A diffusion model is a flow model with $\sigma_t \neq 0$.

# Training Target
We need to define some function $u_t^{target}(x)$ so that we can compute a loss against $u_t^{\theta}(x)$, so that the SDE converts $p_{init}$ to $p_{data}$.

## Conditional and Marginal Probability Path
First, we introduce the idea of a probability path. We start with an initial distribution. A convenient one is $N(0, I_d)$. Then, we create a new function of time that spits out a distribution. It has the following properties.
- $p_0(\cdot | z) = p_{init}$
- $p_1(\cdot | z) = \delta_z$
One example of distributions that might have this property, are, if we have continuously differentiable functions $\alpha_t, \beta_t$, where $\alpha_0 = \beta_1 = 0$ and $\alpha_1 = \beta_0 = 1$, then consider $N(\alpha_t z, \beta_t I_d)$. It has the nice shifting morphing property we are talking about.
However, if we first sample $z$ from $p_{data}$, and then sample from this marginal probability function, we will get a function that morphs from $p_{init}$ to $p_{data}$!
## Conditional and Marginal Vector Fields
The continuity equation from physics helps us understand how these probability distributions morph. We have $\partial_t p_t(x) = - \text{div}(p_t u_t^{target})(x)$. As the probability distribution changes, $u_t$, the flow, directs it. But, it is often easier to compute $u_t^{target}(x|z)$ for a specific ending value. We can sum over, to get the average, by doing:
$$ u_t^{target}(x) = \int u_t^{target}(x|z) \frac{p_t(x|z) p_{data}(z)}{p_t(x)} $$
To understand this, consider that $p(z|x) = \frac{p_t(x|z) p_{data}(z)}{p_t(x)}$ by Bayes identity.
That is, given $x$, we then know the probability that $z$ will "be there" at that point, or how much of $z$ will be coming from there. Thus, we can say how much "flow" at $x$ is coming from the streams going to $z$, which is precisely the data we know from $u_t^{target}(x|z)$.
Here:
$$X_0 \sim p_{init}, \ \frac{d}{dt}X_t = u_t^{target}(X_t | z) \implies X_t \sim p_t(\cdot | z) $$
We can use this expression, with knowledge of our desired $p_t(\cdot | z)$ to compute $u_{t}^{target}(x)$.
We also compute the marginal flow for a Gaussian. To understand it, make sure to note that the frame of reference is fixed, as the mean of the Gaussian moves, and we get ever higher rates of compression as the whole plane's probability distribution comes rushing towards the point z. That helps us understand the term $\frac{\dot \beta_t}{\beta_t} \alpha_t$... it is tracking the velocity at point $x = 0$, to account for the fact that the mean is moving away from the origin so we need more velocity to move everything in that direction.3
## Conditional and Marginal Score Functions
The question becomes, when we add Brownian noise, how can we be sure that the probability distribution of where we expect to be will still be $p_t(x)$?
The answer: the Fokker-Plank equation states that, when the dynamics are described by an SDE, the correct $u_t(X_t)$ that will get us to the probability path $p_t(x)$ that we want will satisfy the following equation:
$$\partial_t p_t = -\text{div}(p_t u_t)(x) + \frac{\sigma^2_t}{2} \Delta p_t(x) $$
Grinding out the algebra, starting from the continuity equation which fully describes how we want $p_t$ to morph over time, we end up with:
$$ \partial_t p_t(x)  = - \text{div} \left( p_t \left[ u_t^{target} + \frac{\sigma^2_t}{2} \nabla \log p_t \right] \right)(x) + \frac{\sigma_t^2}{2}\Delta p$$ This has the form of the Fokker-Planck equation, as desired!
Thus, the correct $u_t$ term for the SDE to get the probability morphing that we want, is
$$ dX_t = \left[ u_t^{target} (X_t) + \frac{\sigma_t^2}{2} \nabla \log p_t (X_t) \right]dt + \sigma_t dW_t$$
The marginal score function (which is needed for this SDE) can be computed from the conditional score function:
$$ \nabla \log p_t(x) = \int \nabla \log p_t (x|z) \frac{p_t(x|z) p_{data} (z)}{p_t(x)} dz $$
Here, we recognize by Bayes law, again, $p_t(z|x)$ as the factor in the fraction.

# Training the Generative Model
For the ODE problem, we want to minimize the loss:
$$ \mathcal{L} (\theta) = \mathbb{E}_{t \sim \text{Unif}, x \sim p_t} [ \| u_t^{\theta} (x) - u_t^{target} (x) \|^2] $$
However, computing $u_t$ is intractable, even though we have an analytical formula for it:
$$ u_t^{target} (x) = \int u_t^{target}(x|z) \frac{p_t (x|z) p_{data}(z)}{p_t(x)}dz $$
Therefore, we in a way "sample" so that we are computing this integral implicitly, by comparing against the conditional velocity field instead:
$$\mathcal{L}(\theta) = \mathbb{E}_{t \sim \text{Unif}, z \sim p_{data}, x \sim p_t (\cdot | z)} [ \| u_t^{\theta} (x) - u_t^{target}(x|z) \|^2] $$
Intuitively, it makes sense: in randomly sampling $z$, if the flow directions of the conditional targets go against each other, they will balance out eventually.
This is an especially simple computation if we are dealing with the Gaussian distribution.

If we want to extend this to the SDE problem, we will add the score matching term. But this term needs to be learned! So we learn it in the same way: learning the conditional score matching term first, and then learning the marginal term. We thought of this score matching as the correction we needed in order to ensure the stochasticity didn't take us away from the path we needed to get to. We can again learn the super complicated marginal function by taking the expectation of the conditional functions.

Quick fact: Denoising Diffusion Models are just diffusion models with Gaussian probability paths.

In order to deal with instability, we learn the noise instead, and scale it after the fact (by dividing by $\beta_t$). The noise is the underlying unit Gaussian that is used to generate the noise for the scaled Gaussian.

A property of the Gaussian flow matching problem is that the flow $u$ and the score matching term $s$ are directly related. If we learn one we learn the other.

There are a couple different ways that diffusion models have been thought of in the past.

## Building an Image Generator
Conditional Generation: how can we condition our generator based on text prompts?
Since we were already talking so much about conditioning objects on $z$, we will here instead use the word guided.
That is, when we have a text prompt $y$, we then have that our data distribution should be given by $p_{data}(z|y)$. 
Then, we seek to learn the following function:
$$
u^{\theta} : \mathbb{R}^{d} \times \mathcal{Y} \times [0, 1] \to \mathbb{R}^{d}, (x, y, t) \mapsto u_{t}^{\theta}(x | y)
$$
We sample $(z, y) \sim p_{data}$, instead of just $z$. Then, we minimize the following loss function:
$$
\mathcal{L}_{CFM}^{guided} (\theta) = \mathbb{E}_{(z, y) \sim p_{data}(z, y), t \sim \text{Unif}[0, 1), x \sim p_{t}(\cdot, z)} \| u_{t}^{\theta}(x | y) - u_{t}^{target}(x | z) \|^{2}
$$
If we used Gaussian probability paths, we can write the $u_{t}$ term as:
