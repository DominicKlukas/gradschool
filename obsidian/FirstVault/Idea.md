- Way to transfer over symmetries from one task to another: sub-task symmetry identification.
	- Perhaps once you have identified a symmetry in the task, you can train an equivariant neural network using a non equivariant neural network.
- JEPA: The information required by the lower level network might be fundamentally different from the information required for planning. Perhaps use both information from the actual state, and the first level JEPA for the next level.


- Robots need a significant amount of data to learn from their environment.


- Symmetry breaking: the manipulator's actions are symmetric in 3 space in theory, but the problem is that often the end effector itself constrains the symmetries.
	- Combine an equivariant system with a modifier that maps it onto its action space.


## Papers Read
### Relevant to RL Symmetries
- Meta Learning Symmetries by Reparameterization
	- Let $W$ be the linear, fully connected weight matrix of an MLP. Then, we can flatten $W$ into an $nm$ vector. Now, we can have this flattened $W$ be a linear combination of $nm$ vectors, and write it as $U \in \mathbb{R}^{nm \times k}$, parameterizing it with another vector, $v$. In particular, the idea is that $U$ will be learned such that each column is an equivariance preserving layer, so $v$ is a linear combination of different such columns. Then, when we train our network, we take turns, learning $v$, and learning $U$, so that the right equivariance is learned.
- A Practical Guide for Incorporating Symmetry in Diffusion Policy
	- Compares different ways to bake symmetry into a robotic diffusion policy.
- The surprising effectiveness of equivariant models in domains with latent symmetry
	- They propose three techniques to augment diffusion models without making them fully equivariant:
		- Just replace the CNN with an equivariant CNN
		- Compute the relative trajectories, applying the inverse of the SE3 transformation that gets you to your initial state
		- Create an equivariant function from a non-equivariant function, in the case of a finite group, by taking the average over all the group transformed outputs.
- Symmetry Breaking and Equivariant Neural Networks
	- This deals with something called relaxed equivariance, where if you have a stabilizer of a certain element in the group, in the group you are mapping to you are fine so long as you are in the co-set of the stabilizer corresponding to the group element you are multiplying $g$ by. Essentially, symmetry equivariant up to a transformation.
- Continual Vision-based Reinforcement Learning with Group Symmetries
	- Here, they cite papers (24-27) which define homomorphisms of mdps to smaller mdps, so that you solve the smaller mdp and in doing so solve the bigger one. Group equivariance is a form of such a symmetry.
		- A previous paper done by the same people trains and keeps a set of experts. With a latent variable, determines which expert is most likely to correspond to the current task, or whether a new actor has to be trained.
	- This paper does a similar thing. It uses equivariant PPO architectures for the experts. It uses a group invariant task grouper as well, computing the difference between the given task and tasks seen before to choose an expert or choose to create a new expert.
- A Practical Method for Constructing Equivariant Multilayer Perceptrons for Arbitrary Matrix Groups
	- They derive the equations required for any network to be equivariant, and show that the derived equations are generalizations of the methods used by all the other equivariant neural network papers.

### Semi-relevant to RL Symmetries
- Integrating Symmetry into Differentiable Planning with Steerable Convolutions
	- This is for planning algorithms: they look at a gridworld problem they have never seen before, and have to come up with a plan for it.
	- They show that theoretically speaking equivariant networks are better and also perform better empirically.
### Not Relevant to RL Symmetries
- Learning Invariant Feature Spaces to Transfer Skills with Reinforcement Learning
	- We have two different MDPs for two different robots. But we learn a function that maps the states of both of the spaces to a new space, such that similar states are mapped together. We do so by training two "autoencoders" $f$ and $g$ and then training a loss function that minimizes the distance between the two.
- Combining Local Symmetry Exploitation and Reinforcement Learning for Optimised Probabilistic Inference -- A Work In Progress
	- (Very roughly) When doing probabilistic inference, you aim to find the relationships between random variables in a joint distribution. You can "factor" the distribution into independent parts. But the order in which you do this is very important, and affects the computational cost. You can formulate this problem as an MDP, and by grouping together symmetries (variables which can be exchanged? sub-graphs that look the same? (I suppose variables are leaves of the graphs)) you can share computations and solve the problem more efficiently.
- Equivariant Reinforcement Learning for Quadrotor UAV
	- We transform a state into another state space with lower dimension using a group operation, solve the problem in the simpler state space, and then use the inverse group operation to get back to our original state.
- Symmetry Detection in Trajectory Data for More Meaningful Reinforcement Learning Representations
	- They start with candidate transformations, transform their original trajectories, then use a discriminator network to see if it can learn the difference between the transformed and original trajectories. If the original trajectories were sampled from a symmetric distribution, the two datasets (transformed and original) will be the same.
## Papers to read
- Advanced deep-reinforcement-learning methods for flow control: group-invariant and positional-encoding networks improve learning speed and quality
- Reinforcement Learning with Lie Group Orientations for Robotics
- MDP Homomorphic Networks: Group Symmetries in Reinforcement Learning
- SiT: Symmetry-Invariant Transformers for Generalization in Reinforcement Learning
- Representation and Invariance in Reinforcement Learning
- Invariant Policy Optimization: Towards Stronger Generalization in Reinforcement Learning
- Symmetries-enhanced Multi-Agent Reinforcement Learning
- Exploiting Approximate Symmetry for Efficient Multi-Agent Reinforcement Learning
- Can Euclidean Symmetry be Leveraged in Reinforcement Learning and Planning?
- Koopman Q-learning: Offline Reinforcement Learning via Symmetries of Dynamics
- Port-Hamiltonian Neural ODE Networks on Lie Groups For Robot Dynamics Learning and Control
- Clebsch-Gordan Transformer: Fast and Global Equivariant Attention
- Group Equivariant Convolutional Networks
- Sample Efficient Grasp Learning Using Equivariant Models
- Group Equivariant Deep Reinforcement Learning
	- They implement snake!
	- They use E2? Perhaps use D4 + translation instead?
- PEnGUiN: Partially Equivariant Graph NeUral Networks for Sample Efficient MARL
	- We have one equivariant and one non-equivariant network, with an MLP to learn a parameter which takes a linear combination of the two.
- Shubhendu Trivedi
- Morphological symmetries in robotics !!! Big one
Questions to answer
- If we know the symmetries present, what can be done?


Ideas
- Design an algorithm that can learn the symmetries in an environment.
	- There are already symmetry classification algorithms
	- Learning from latent spaces
		- How can we use this in the context of robotics?
		- How do we determine the information required of us in order to 
- Use subgroup equivariant networks in order to deal with cases of obvious symmetry breaking in manipulation problems (for example, reachability issues).
	- Design networks which are equivariant under specific normal subgroups, but break symmetry in the normal subgroups (between the conjugates).
		- What if the parent group is simple? (Like SO(3)).
			- Can I define regions somehow in which certain symmetries hold? 
	- Will require knowledge of which neural network architectures are profitable.
A little bit more engineering/application/mix and match style
- Use a CNN equivariant under specific groups, and perhaps other architectural changes, in order to improve the performance of the VLAs.
	- Perhaps use group average of pre-trained network for testing


1. What problem does this project solve?  
   This project solves the problem of making use of the sample efficiency of equivariant reinforcement learning/behavior cloning policies when symmetry is broken in certain sub-regions of the orbit of a group action.
2. Who is the target audience of this work? What sub-community will be interested in this work?
   Robotics research communities, Geometric Control, Deep Learning communities
3. What are the core technical and conceptual contributions?
   Novel network design:
	1. In the group convolutions in an equivariant neural network $\sum_{h \in H} f(h) \Phi(g^{-1}h)$, introduce specific symmetry-breaking weights $\sum_{h \in H} \sum_{l \in L, h \in \mathcal{S}} w_{l}(h) \Phi_{l}(g^{-1}h)$, $S < H$, or potentially $S \subset H$. For example, the $C_{n}^{3}$ group... we can make it equivariant under one rotation axis, but not under another. Then, combine as $C_{n}^{3}\rtimes \mathbb{R}^{3}$, or simply as $C_{n}^{3}$ (have to think about that!)
	2. Local equivariance: after learning a specific neural network, instead of convolving across the entire group, convolve over a subset of the group, at any given location. This should enable a type of local-equivariance, instead of enforcing equivariance over the entire orbit of the group action.
		1. Potentially also use the whole group as a prior, progressively weighing convolutions of "more aggressive" group actions as less important.
		2. If you start the weights all at 1, then if you stay in an equivariant regime, if your environment is truly equivariant, then there are proofs which show that it will stay equivariant.
4. What are the technical justifications for taking this approach?  
	1. Equivariant neural networks have shown impressive sample efficiency in robot manipulator problems, especially in RL problems, and behavioral learning problems, significantly outperforming traditional learning methods. However, they require that symmetry holds inside the entire domain, which can be detrimental in situations where symmetry is broken in an environment requiring different trajectories for similar tasks in different orientations, due to kinematic constraints or obstacles. Finding a way to train a general policy that makes use of this is difficult.
5. What can we now do that wasn’t possible before? What are the benefits of this method? 
	1. Now, we can train models that have the sample efficiency of equivariant models with the ability to break their constraints, in the context of robotic manipulation problems, which has never been done before.
6. What are some previous methods and why couldn’t they do the same things?
	1. Previous symmetry breaking RL equivariant models were not very sophisticated: a simple learned linear combination of an equivariant model and a non-equivariant model, in the context of mutli-agent learning.
7. For each contribution / benefit of the method(s), describe the example(s), simulation(s) and/or experiment(s) that will showcase this benefit clearly.  
8. Why would somebody else use this work or build on it?  
9. What are the limitations of the work, and for each limitation, how will it be addressed?  
10. What is the single most important point that you want a reader to take away from a paper  
on this project?