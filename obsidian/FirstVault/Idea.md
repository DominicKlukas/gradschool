- Way to transfer over symmetries from one task to another: sub-task symmetry identification.
	- Perhaps once you have identified a symmetry in the task, you can train an equivariant neural network using a non equivariant neural network.
- JEPA: The information required by the lower level network might be fundamentally different from the information required for planning. Perhaps use both information from the actual state, and the first level JEPA for the next level.


- Robots need a significant amount of data to learn from their environment.


- Symmetry breaking: the manipulator's actions are symmetric in 3 space in theory, but the problem is that often the end effector itself constrains the symmetries.
	- Combine an equivariant system with a modifier that maps it onto its action space.


## Papers Read
- A Practical Guide for Incorporating Symmetry in Diffusion Policy
- The surprising effectiveness of equivariant models in domains with latent symmetry
- Symmetry Breaking and Equivariant Neural Networks
	- This deals with something called relaxed equivariance, where if you have a stabilizer of a certain element in the group, in the group you are mapping to you are fine so long as you are in the co-set of the stabilizer corresponding to the group element you are multiplying $g$ by. Essentially, symmetry equivariant up to a transformation.
## Papers to read
- Advanced deep-reinforcement-learning methods for flow control: group-invariant and positional-encoding networks improve learning speed and quality
- Reinforcement Learning with Lie Group Orientations for Robotics
- Continual Vision-based Reinforcement Learning with Group Symmetries
- MDP Homomorphic Networks: Group Symmetries in Reinforcement Learning
- SiT: Symmetry-Invariant Transformers for Generalisation in Reinforcement Learning
- Representation and Invariance in Reinforcement Learning
- Invariant Policy Optimization: Towards Stronger Generalization in Reinforcement Learning
- Learning Invariant Feature Spaces to Transfer Skills with Reinforcement Learning
- Combining Local Symmetry Exploitation and Reinforcement Learning for Optimised Probabilistic Inference -- A Work In Progress
- Symmetries-enhanced Multi-Agent Reinforcement Learning
- Exploiting Approximate Symmetry for Efficient Multi-Agent Reinforcement Learning
- Can Euclidean Symmetry be Leveraged in Reinforcement Learning and Planning?
- Symmetry Detection in Trajectory Data for More Meaningful Reinforcement Learning Representations
- Koopman Q-learning: Offline Reinforcement Learning via Symmetries of Dynamics
- Port-Hamiltonian Neural ODE Networks on Lie Groups For Robot Dynamics Learning and Control
- Clebsch-Gordan Transformer: Fast and Global Equivariant Attention
- Group Equivariant Convolutional Networks
- Equivariant Reinforcement Learning for Quadrotor UAV
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