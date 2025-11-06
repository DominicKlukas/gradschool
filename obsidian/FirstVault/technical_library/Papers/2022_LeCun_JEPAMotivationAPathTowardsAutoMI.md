---
tags:
  - technical_library
title: A Path Towards Autonomous Machine Intelligence
authors: Yann LeCun
bibtex:
pretty_cite:
link: https://openreview.net/pdf?id=BZ5a1r-kVsf
topics: DL, Self-Supervised Learning, World Models, Planning
reading_lists:
projects:
type:
to_read: false
stars:
---
Goal: how to move forward to agents that can abstract away info for planning at multiple levels.

# Introduction
- Humans can learn much faster, with much, much less data, than AIs can.
- Why? Perhaps they have internal world models of how the world works.
What are the challenges AI research must address today?
- How can we learn as much as possible from observation, so that expensive, dangerous real-world trials don't have to be relied on so extensively?
- How can planning/reasoning be made compatible with the gradients used to efficiently improve loss functions?
- How to plan at multiple levels/time frames.
This paper suggests architectures and paradigms that address each of these points.

## Learning World Models
- Common sense tells humans and animals what we can and can't do.
- MPC has a world model that predicts what can and can't happen, but this idea has been neglected in RL.
- It thus makes sense to allow machines to learn their own unsupervised world models, and use them to predict, reason and plan.
- The nature of Human's internal world models and understandings of physics is exposited.

### Model Architecture for Autonomous Intelligence
- It contains a few components: configurator, world model, actor, perception, cost, short-term memory.
	- Configurator: meta parameters, to tailor all components to the process at hand
	- World model: predicts future states and had different reps for different hierarchies of tasks/plans, and fills in data missing from perception, perhaps using short term memory.
	- Actor: gives sequence of actions to world model (to train through gradient descent)
	- Cost: critic uses world model's predictions to compute future cost. Intrinsic cost is short term/current pain/pleasure
	- Short term memory stores helpful information, for the world model
	- Perception: boils down the state of a world from the input data.
- This architecture mirrors how people learn/the human brain works.
They talk about two modes in which this architecture can act: in the first, the actions are unaffected by the world model/cost, and simply act deterministically from the perception/short term memory.
Mode 2 is when you optimize the actions in the world model, using the cost critic to predict future state's cost functions.
You can mix them: optimize the action using mode 2 and then eventually fix the parameters and use mode 1.
- The rewards are linear combinations of functions, with weights determined by configurator, the trainable part being the critic and the immutable part being the intrinsic cost.
- They then argue that learning by objectives is best: it holds regardless of whether the environment changes, and minimizes hard-wired design.
### Training the Critic
- You can store previous intrinsic values, and take interpolations of them to make predictions for other states/times.
- This is similar to the A2C architecture for RL.

## Designing and Training the World Model
- We want our world model to give a probability distribution over multiple possible next states, not just a single state.
- We want different time scaled and levels of abstraction, mimicking the way that humans learn.
- We want to take actions in our training set that will result in as diverse as possible a training set.
- SSL, or self supervised learning is essentially patter prediction.
	- Example: Video completion prediction: what is the probability video y is the second half of video x.
	- Energy based methods: train a scalar function that compares x and y, and is lower if it is more likely that they are connected.
	- Our latent space should have the property that, given a state x and a future state y, y can be easily predicted from x. A latent space should contain all the information necessary to make this inference.
	- We also can have latent variable energy based methods, where some third variable is minimized: $\hat{z} = \text{argmin}_{z \in \mathcal{Z}} E_{w}(x,y,z)$ and then the energy value for this $\hat{z}$ is taken as the energy.
### Energy based methods
- We continue the line of thought. The energy function can be trained with a DL network.
- We don't want the function to collapse: give the same low energy to all predicted states.
- If the latent space $z$ in a latent variable energy based method has too high dimension, then we can have a problem where y collapses, if the dimension of y is low in comparison to $z$.
- How can we prevent collapse?
	- Contrastive methods: your loss term is a function that spikes around the true prediction of x like a softmax function, and have high energy for fake data generated (contrastive samples). For instances, swapping $y$'s for different $x$'s.
	- Regularized methods have the energy of true samples low, but then try to keep the function itself as high as possible. (for instance, having a loss 1 - e^x^2 minimized over the entire sample. I made that one up don't trust it).
## JEPA
The following architecture is used.
- Two encoders: one for x and one for y.
- Predictor that takes x and a latent variable z to predict y.
- Compare prediction to the given y, minimizing predictions over latent variable z.
We have to make sure that the encoders store as much info as possible to prevent collapse, that the prediction of $s_{y}$ is made easily from $s_{x}$, and that $z$ stores as little information about the state as possible (so that every prediction can't be optimized simply by choosing an appropriate $z$, making the states $s_{y}$ meaningless. Let the reader understand.)
These can be achieved, for example, by adding penalties to the sizes of the $z$ vectors.
- The way that we ensure that $s_{x}$ and $s_{y}$, we ensure that they have good data coverage, is by transforming them, through a neural network we also train, to a slightly higher dimensional variable, and then make sure the variance of the elements is in the range we want when we vary the dataset, and the covariance between elements in the higher dimensional variable is also high.
	- If the covariances are not high, then we may have a low dimensional subspace housing all the data in some other basis
For heierarchical planning, you use a JEPA on top of the JEPA, working on your embedding  $s$ instead of the raw data $x$. They can also be sampled at different timescales, in order to train them for different levels of planning/control.
### Hierarchical Planning
- Higher level actions, as well as lower level actions, are both learned. The higher level actions are targets for the lower level predicted states. 
- Key to understand: the states being predicted at each next level are different for the different levels. 
- The actions aim to present a desired state for the level below, which the actor on the level below is trying to minimize the cost function for.
### Handling Uncertainty
- There are many different types and sources of uncertainty.
- Use the latent variable as a means of running through the distribution of the states.
- You can also sample this distribution, and run a Monte Carlo Tree Search in the latent space. MCTS ensures that all actions from a particular node are visited.

Actions themselves shouldn't be random.
Models used inside of JEPA should match the models.

## Memory and World State
Often, only a small part of our world changes with an action.
The problem with having the entire world as a single vector space, is that you have to modify the whole thing even if you do something small.
Therefore, having a key value system, where each vector, or a number of subdimensions of the world's vector space, has a key attributed to it so it can be accessed, and a mapping is learned between keys and dimensions of the vector space.
If we have a certain key corresponding to a certain action or task, then we learn which parts of our memory are relevant to that key.

We can also wonder about data streams: how much can we learn from just passive observation? Are there things where, in order to learn them, we need to actively interact with our environment?