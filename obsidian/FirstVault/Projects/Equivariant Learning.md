# Background
A property of an object is symmetrical under a specific transformation, if after applying the transformation the property stays the same. For example, a ball looks the same regardless of how you rotate it: it is symmetrical under rotations. You can flip an equilateral triangle about its median without changing it.

Symmetries can often be modeled as linear transformations on vector spaces. For example, the rotation matrix $$
R(\theta) = \begin{bmatrix}
\cos\theta & -\sin \theta\\ \\
\sin\theta & \cos\theta
\end{bmatrix}
$$
rotates vectors in $\mathbb{R}^{2}$. Similarly, you can flip the vector space about the $x$-axis with the following transformation:
$$
F = \begin{bmatrix}
1 & 0  \\
0 & -1
\end{bmatrix}
$$
Then, we can flip about an arbitrary axis by compositing these matrices: $R(-\theta) F R(\theta)$. If our object is symmetrical under rotations and flips, then our object is symmetrical under this composed transformation as well. Therefore, given a certain set of transformations, we can generate more transformations under which the object is symmetric.

This is the motivation behind group theory. A group is a set $G$ with an operation $\star$ such that for any $g, h \in G$ and $g \star h \in G$, that satisfies three properties: $\exists e \in G$ such that $e \star g = g$ for all $g \in G$, for each $g \in G$ $\exists g^{-1}$ such that $g \star g^{-1} = e$, and $g_{1} \star (g_{2} \star g_{3}) = (g_{1} \star g_{2}) \star g_{3}$. These are the properties we might expect for a symmetry: 
- $e$ represents the identity transformation.
- If we apply a transformation $g$ under which an object is symmetric, undoing the transformation obviously will be a symmetry.
- The order in which we group multiple transformations has no effect on the outcome. This is different from commutativity, which says that we can swap the order of the elements themselves as well as the order of operations, which is not always true. The Dihedral groups are a classic example.

At this point, we may ask: what is the benefit of this abstract representation? Why not stick with linear transformations? Why must we consider groups?

The answer lies in the fact that we may deal with different representations of data when we are trying to apply the transformations under which we are symmetric. For example, suppose we are situated in $\mathbb{R}^{3}$, and we have an operation which is symmetric under rotations through the $z$-axis. Then, the group of rotations might be represented as
$$
R(\theta) = \begin{bmatrix}
\sin \theta & \cos \theta & 0 \\
-\cos \theta & \sin \theta & 0 \\
0 & 0 & 1
\end{bmatrix}
$$
But then, we may realize that we aren't interested in the $z$-axis at all, so we instead work in $\mathbb{R}^{2}$, where our transformation is represented by the 2D rotation matrices.
We write these representations as $\rho(g)$, where the space on which $\rho$ acts is made clear from context. 

We may also work with discrete groups. For instance, instead of the set of continuous rotation transformations, we may consider only the rotations that preserve a square, which are rotations that are multiples of 90 degrees.

In the context of MDPs, we typically have two spaces that we work with: the action space, and the state space.
A given transformation may act differently on these spaces. Let $\rho_{s}$ and $\rho_{a}$ denote the representations on $\mathcal{S}$ and $\mathcal{A}$ respectively. For example, if we are driving a car down a road and we turn right, a flip about the centerline of the road will show the car turning left, but also the steering wheel turning left: both the action space, that is, the angle of the steering wheel, and the car itself, will have flipped, but they may have flipped differently.

We say that an MDP is $G$-invariant if the transition function $T$ has the property that $T(s' | s, a) = T(\rho_{s}(s') | \rho_{s}(s), \rho_{a}(a))$ and $R(s, a) = R(\rho_{s}(s), \rho_{a}(a))$. It can be shown that, if this is the case, then the optimal policy is equivariant. That is, $\pi^{*}(\rho_{s}(s)) = \rho_{a} (\pi^{*}(s))$

The promise of equivariant RL is that, by taking advantage of this equivariance property, we can reduce our sample space, and learn more quickly and generalize more effectively.

# Equivariant Neural Networks
Since we deem the equivariance property, that is, $\pi(\rho_{s}(s)) = \rho_a (\pi(s))$, to be a useful prior, we ask, how can we design neural networks that have this property build in? One answer is, steerable convolutional neural networks. 

First, we recall how CNNs work. Convolution is a mathematical operation, defined in the continuous case by the integral
$$
(f * k)(\vec{x}) = \int_{\mathbb{R}^{2}} f(\vec{t})k(\vec{t} - \vec{x}) \vec{d}t
$$
where $f : \mathbb{R}^{2} \to \mathbb{R}$, and $k : \mathbb{R}^{2} \to \mathbb{R}$ is called the kernel. By thinking of a few common examples:
- $k(\vec{x}) = \delta_{a}(\vec{x})$
- $k(\vec{x}) = \exp(-\lvert \vec{x} \rvert^{2})$
- $k(\vec{x}) = \exp(-i \vec{\omega}\cdot \vec{x})$
We can see that it makes sense to think of $k$ as a filter of sorts, that extracts certain features from our data. Typically, in CNNs we will be interested in extracting many features, so a CNN will have many layers: copies of the original dataset after specific (different) features have been extracted.

Naturally, we don't work with continuous datasets, but rather discretizations of our dataset, and so approximate the integral with:
$$
(f * k) ( \vec{x}) = \sum_{\vec{t} \in \mathbb{Z}^{2}} f(\vec{t}) k(\vec{x} - \vec{t})
$$
In order to make a CNN equivariant under transformations, we first need to define how the group acts on the input space. An easy example might be rotations of a square image. A more creative example might be permuting subregions of an image. Either way, in the case of a discrete group, we collect all of the ways in which the group acts on the image: $g_{1}, g_{2}, g_{3}, \dots, g_{n}$.
Then, for any feature kernel $k$ which feeds into some output channel $C$, we create $n$  copies total of the output channel which arise as a result of the same feature kernel, but then transform input into the convolution by $g_{i}$ for $2 \leq i \leq n$ before inputting it into the convolution.
![[Pasted image 20251112155835.png]]
In this diagram, the group $G$ consists of the 4 elements $\theta_{0}, \theta_{90}, \theta_{180}, \theta_{270}$. We can see that the kernel extracts the feature $e$ differently in different output channels. In this diagram, $H$ denotes the output feature space (the output channels).
Now, an important question is: when we transform the original image according to the group, what happens to our output feature space?
- Rotate the image by 90 degrees, and count the orientations of the resulting features
	- We get one feature at $90$ degrees in the top left corner, and two features in the middle bottom right of the image rotated at 180 degrees.
- Then, we can see that the output data in $C_{\theta_{0}} \to C_{\theta_{90}}$, and $C_{\theta_{90}} \to C_{\theta_{180}}$, and so on for the rest of the channels. However, we note that, in the group, $\theta_{0} \star \theta_{90} = \theta_{90}$, and $\theta_{90} \star \theta_{90} = \theta_{180}$. Therefore, applying a group operation to our original image results in permutations of the output channels, which are consistent with their group labellings!

How do we write this operation?
$$
C_{g}(\vec{x}) = \sum_{\vec{t} \in \mathbb{Z}^{2}}  f(\vec{t})k(\rho_{s}(g^{-1})(\vec{x} - \vec{t}))
$$
We may also have multiple different kernels, so the output channel is stack of $n|G|$ outputs from these kernel operations.

Once we have "lifted" our data to a feature space whose channel count is some multiple of $|G|$, and by construction applying the group representation onto the input data results in permutations of the channel indices according to the group structure, we can create deeper channel layers as follows by applying a similar operation to individual kernel layers.
However, the caveat here is that the group convolution operator must be equivariant to both group actions in the spatial domain, and the permutations of the channels themselves. Then, for a channel $C_{g}^{out}$ in the output feature space corresponding to the group element $g$, with $N |G|$ input channels, the desired convolution operation will be:
$$
C_{g}^{out}(\vec{x}) = \sum_{n=1}^{N} \sum_{h \in G} \sum_{\vec{t} \in \mathbb{Z}^{2}} C_{h}^{in}(\vec{t}) k_{n}(\rho_{s_{1}}(g^{-1})(\vec{x} - \vec{t}), g^{-1} \star h)
$$
Here, I denote $s_{1}$ to mean the spatial dimensions of the input channels, since this might be smaller (convolution tends to shrink the sizes of the spatial dimensions) than the original space.
This then ensures the equivariance property, throughout all of the layers. Between these layers, we can apply a ReLU function, and even max-pool operations (but there are nuances in how these functions are applied, so as not to disturb equivariance).

# Learning Symmetries
First, we may ask, are there any ways to automatically determine if symmetries are present in a dataset, so that models that rely on equivariance are less dependent on the inspiration of the designer to make use of symmetries?
### Meta Learning Symmetries
Our first observation, is that the convolution operations in steerable CNNs require that the weights of multiple channels are tied together. Namely, whereas in a standard CNN the kernels between different channels are free to be completely independent, for steerable CNNs, kernels are the same (after rotation) and tied together in groups of $|G|$ channels. Therefore, steerable CNNs are a subset of normal CNNs.

Furthermore, we can also roughly consider steerable CNNs to be constructed out of a set of equivariant basis functions, since adding sets of weights together for two equivariant neural nets will result in yet another equivariant neural net.
Then, suppose we flatten all of the weights $W$, into one massive vector, $\text{Vec}(W)$. We can consider taking linear combinations of different weights vectors, while keeping the weights in the individual vectors themselves fixed:
$$
\text{Vec}(W) = \begin{bmatrix}
\text{Vec}(W_{1}) & \text{Vec}(W_{2}) &\dots & \text{Vec}(W_{n})
\end{bmatrix}^{T} \cdot  \vec{v}
$$
where $\vec{v}$ is some $n$-dimensional scalar vector. In [[2021_Zhou_MetaLearningSymmetries]], they have two training loops. First, they learn $\vec{v}$, for a given set of weight matrices $\{W_{i} \}_{i}$. Then, they fix $\vec{v}$, and adjust the $\{ W_{i} \}$ (or some lower dimensional factorization of these matrices to save space). The idea is that this will give the model a chance to learn the appropriate symmetries by itself, without requiring them to be specified or even known beforehand.

[[2025_DLSymmetryLearningTheory]] learning theory: this paper I haven't read, but looks interesting.
## Classifying Symmetries
[[2022_DAlonzo_SymmetryDetection]] try to classify which symmetries are present in a dataset, instead of learning them implicitly. They transform the dataset according to a symmetry in a chosen group of symmetries, and train a discriminator network that aims to characterize the difference between the transformed and original network. If it can't tell the difference, then the given symmetry applies! [[2023_Karjol_SymmetryDiscoveryFramework]] does something similar but more complicated and nuanced. I haven't read it yet.
## Latent Symmetry Spaces
### Transition Model Learning
In [[2022_Park_LearningSymmetryEmbeddingsEquivariantWorldModels]], we have an input state space which is not equivariant under a certain symmetry, but we know that a certain symmetry exists under the hood. We learn a latent space, and a transition function using the contrastive loss between the output of the transition model, and the actual next step (in a self-supervised kind of way) to get good embeddings.
In this model, we learn a latent space, and a transition model on that latent space, which describes a latent space in which the dynamics satisfy the equivariance property. ![[Screenshot2025-11-13_11-12-21.png]]
## Latent Symmetry Classification

In the paper [[2024_Yang_LatentSpaceSymmetryDiscovery]] they combine the ideas of using an encoder with the idea of using a discriminator from the classifying symmetries paper, and also create a decoder to be able to reconstruct the original images. This paper also has a really good literature review. Worth looking at more closely!

## Latent Symmetry Equivariant Model Effectiveness
In this paper, [[2023_Wang_EquivariantExtrinsicLatentSymmetry]] we define two types of symmetry breaking: extrinsic, and intrinsic. In extrinsic symmetry breaking, applying symmetries to the data results in states that are not in the orbit of the truth of how the symmetry is applied to the real system. For example, if we rotate the image, that will result in different data than if we rotate the teapot in our image. The rotated image is never a state that can be achieved by rotating the teapot in any which way. They show that applying equivariant models to this type of extrinsic symmetry breaking is very effective, even more so than using vanilla models.
# Equivariant Robotics and RL
Robotics is a fruitful field of application for equivariance, since the physics behind a robot's dynamics, and the tasks we may require a robot to perform are often rich with symmetries: that is, the same after a translation or rotation. Traditionally, brute force methods such as data augmentation would be used to force the models to learn the symmetries in our models. But with equivariance neural networks, they are learned automatically as an inductive bias without the need for extra data or training. Furthermore, robotics problems can make use of this extra sample efficiency, given how expensive trajectories can be to collect.

## Papers Primarily Showing Experimental Results
Most of these papers follow the same pattern: we have some RL problem, and the model has some well defined symmetry in it. We then compare the performance of a deep RL model with a model whose networks are swapped with equivalent equivariant networks.
**NOTE**: It is hard to determine what a "fair" comparison is: do we want a network with the same number of channels, or a network with the same number of trainable parameters?

- [[2020_Mondal_GroupEquivariantDRLAtari]] In this paper they train on some basic atari games that exhibit symmetry, and show sample efficiency/learning rate improvements.
- [[2022_Wang_OnRobotEquivariantLearning]] Here, they show that equivariance enables them to be so sample efficient, that without prior training, they can train a robot to successfully perform pick and place tasks after 1.5 hours of learning.
- [[2022_Wang_S02EquivRL]] Very similar to the last paper, except in simulation with more extensive comparison of RL models. Also, shows that we can choose different groups (we don't have to do S02, we can use some subgroup and then use data-augmentation!)
- [[2023_Wang_EquivariantExtrinsicLatentSymmetry]] As mentioned earlier, they test the hypothesis that equivariant models work well (in robotics problems) even with extrinsic symmetry breaking.
- [[2023_Zhao_EuclidanSymmetryRLAndPlanning]] Haven't read carefully but I assume they are doing more mathematical reasoning about equivariant MDPs, and in particular apply to reacher problems, and also use the E2 group (translation invariance) not just rotation invariance.
- [[2025_Wang_PracticalEquivariantDiffusionPolicy]] Here, they show how equivariance can be used with bigger models easily by showing some simpler engineering-like hacks so that it can be used in conjunction with many different (bigger) models.
- [[2023_Zhao_DifferentiablePlanningWithEquivariance]] They use equivariant networks with planning problems (gridworld problems where the network has to find gridworld solution to a world it has never seen before).
## Slightly more advanced ideas
- [[2022_Liu_CRLWithGroupSymmetries]] This is essentially meta-learning, where you have multiple policies, and new policies can be spawned if the algorithm determines the new task it is trying to learn to be too different from all the ones it has seen previously before, except that it uses equivariant networks in its policies for better sample efficiency. The task grouper (manager?) is also group invariant, so it does not spawn new policies if it isn't the same as what it has seen before.

# Symmetry Breaking in Robotics
## Symmetry Breaking Architectures
First, we look at the paper [[2025_Park_ApproxEquivRL]]. Here, they modify the convolution kernels, in the following way:
$$
C_{g}^{out}(\vec{x}) = \sum_{n=1}^{N} \sum_{h \in G} \sum_{\vec{t} \in \mathbb{Z}^{2}} w(h) C_{h}^{in}(\vec{t}) k_{n}(\rho_{s_{1}}(g^{-1})(\vec{x} - \vec{t}), g^{-1} \star h)
$$
Here, they add in another function, $w(h)$ which breaks the group symmetry. This idea was introduced in [[2024_Kaba_SymmetryBreakingEquivariantNeuralNetworks]]. This is to be learned. They show that, in the case of perfect symmetry, if you initialize the weights such that $w(h)$ is equivariant (all 1's for example), then it will stay that way.

Next, we consider PEnGUiN [[2025_McClellan_PEnGUiNPartialEquivariantNetwork]], where we learn an MLP based on our location that takes the linear combination of two networks, one that is equivariant, and one non-equivariant.
# Symmetry in the Kinematics of Robots
This paper considers the physical symmetries present in a robot [[2025_Apraez_MorphologicalSymmetriesInRobotics]].
