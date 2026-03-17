### Introduction
Today, I will be introducing a topic called Geometric Deep Learning, roughly following the paper Geometric Deep Learning: Grids, Groups, Graph, Geodesics, and Gauges. Geometric Deep Learning is a view of deep learning which motivates the design and explains effectiveness of Deep Learning architectures, as they are applied to different use cases. With it's strong theoretical basis and deep explanatory power, I am convinced it is a interesting and helpful thing to know about.

Why am I talking about this here?

This here, is the classical optimal control problem formulation. We have our state evolving with respect to some dynamics function which is a function of the current control signal and state, and we are trying to minimize some const function which tells us whether or controller is doing a good or a bad job.

If our dynamics are linear, or we understand the physics of our system well with nice laws, we might have a good shot at solving this problem analytically. But what if that isn't the case: our function $f$ might be really complicated and difficult to describe analytically.
This is where deep learning comes in: if we have a lot of data, about how our function is supposed to behave, we can use a parameterized set of functions $\mathcal{F} = \{ f_{\theta} \}_{\theta \in \Theta}$.

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


## Overall Flow of the Talk
What is Geometric Deep Learning
- Neural Networks are an important thing to learn about.
- The framework of Geometric Deep Learning is helpful to understand them.
What is Learning?
- Class of functions we use to approximate our function. Loss function. We then use gradient descent of some sort to 
- Universal approximation theorem.
What is an inductive bias?
- Learning an arbitrary high level function is very difficult.
- Even if we assume Lipschitz continuous, we still have a hard time! Our functions are very complicated in reality.
- If we regularize to make sure our functions are less complex, or even SGD, will tend towards the functions which have smaller parameter complexity.

Geometric Learning: Introducing the Framework
There are three underlying principles between the design of most successful Deep Learning architecture frameworks, that help overcome the curse of dimensionality and introduce helpful inductive priors.
- Symmetry
	- Perhaps go into applications here.
- Geometric Stability
	- If we are close to a symmetry, but not exactly at a symmetry, we don't want our output to vary widely.
	- On the other hand, if our domain changes slightly (for example, if we are on a graph based neural network, we don't want things to change to quickly if our graph shape changes slightly) so if some metric is defined between the graphs then we can be in trouble.
- Scale Separation
	- Why do we make our neural networks deep?
	- Scale separation of functions: This is what we do when we do pooling of any sort.
Now, talk briefly about how Deep Learning Architectures implement each of these three elements.


As always, you may be asking yourselves, what is the point of all of this abstraction?
The point is, that for many deep learning frameworks, this unifying blueprint explains their design. So, next time you have some data to crunch, by asking yourself what inductive bias is the most appropriate, you can have yourself an architecture that learns as effectively as possible?


Visualize the zoo of different types of geometry. How did we understanding the field.
Have outlook of the application. (Not the most crucial thing).