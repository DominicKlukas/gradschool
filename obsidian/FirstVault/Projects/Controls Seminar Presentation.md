### Introduction
Today, I will be introducing a topic called Geometric Deep Learning, roughly following the paper Geometric Deep Learning: Grids, Groups, Graph, Geodesics, and Gauges. Geometric Deep Learning is a view of deep learning which motivates the design and explains effectiveness of Deep Learning architectures, as they are applied to different use cases. With it's strong theoretical basis and deep explanatory power, I am convinced it is a interesting and helpful thing to know about.

Why am I talking about this here? I will take it as a given that Deep Learning, when used correctly, is a useful tool, even in controls.

Introduce the problem
In RL, we might have dynamics functions that are so complicated that we cannot learn them.
Or, we might have very complicated data to deal with, which is still an important part of our control stack.
Either way, in many control scenarios, the appropriate thing to do is to use a neural network.
But which neural network should we use?

There is a massive zoo of deep neural networks we could use to learn approximators for our functions from data.

Today, I will be going through a tutorial which is helpful for understanding what types of deep neural networks there are and when to use each of them. It also presents a unifying framework which explains why different neural networks were designed the way they were in the first place, and draws profound analogies between them. Today, friends, I welcome you to the world of Geometric Deep Learning.

# Introduction to Learning in High Dimensions

Problem formulation: supervised learning: we have a function $f(x) = y$ over some data distribution. Here, we have $X$ being some high dimensional space.
The assumption is, that there is some unknown function $f$ such that $f(x_{i}) = y_{i}$ for every sample $x_{i} \in X$.
Our problem is now approximating $f$ from a parameterized set of functions $\mathcal{F} = \{ f_{\theta} \}_{\theta \in \Theta}$. 

First question: can we use any function in classes we might use for neural networks to approximate any function? The answer is yes. General approximation theorems do the trick for us.

Important: Gradient will choose the weights which minimize the $L_{2}$ norm. 