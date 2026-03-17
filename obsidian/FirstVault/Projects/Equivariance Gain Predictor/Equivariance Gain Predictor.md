## Idea
You have an observation $\mathcal{O}$. In the given observation, you don't have meaningful equivariance. However, if you transform the space, you can define a set of transformations on that space which work nicely. I would like to be able to measure the effectiveness of different representations/task spaces.

Research question: which representation changes expose useful underlying group structures which can be exploited by robotics sensors/observations that may otherwise have nuisance variations, with non-linear global symmetries?

Hypothesis: representations which have high "sample efficiency measure" will in general perform better than representations that have lower sample efficiency measure, with "sample efficiency measure" defined in a useful way.

Goal of paper
- Determine a metric which is useful, easily testable, and will predict whether a given representation is helpful in a specific environment (a good predictor of sample efficiency gains for a specific type of equivariant constraint).
# Background

Often, RL tasks will have some sort of map to get you into a geometric representation where symmetry groups and helpful and useful, so that the inductive bias induced by the equivariant architectures and helpful.
## Inspirational Papers to Read,
- Lift Splat Shoot
	- Use CNNs to determine the height/location of different pixels from different cameras to create a birds-eye view
- RAVEN: End-to-end Equivariant Robot Learning with RGB Cameras
	- Represent pixels in ray form, and then compute attention w.r.t. geometric distance between rays
- EquivAct: SIM(3)-Equivariant Visuomotor Policies beyond Rigid Object Manipulation
- Improved Canonicalization for Model Agnostic Equivariance
- Learning Invariant Representations for Reinforcement Learning without Reconstructions
## Types of Maps
### Differentiable Warps
These are maps which take an image and map it to another image using a neural network defined as $\phi(x) = I(W_{\theta}(x))$, using a continuous representation of the image (Bi-linear Interpolation) so that gradients flow.
### Canonicalization
Mapping every observation to a canonical representative of its symmetry class.
### Neural Fields
#### NeRFS
In 3-space you have a different color/density at every point. You determine different camera angles by integrating along rays (throughout all space).
#### Signed Distance Functions
A function $f(x)$ with $f(x) = 0$ on the surface, $f(x) > 0$ outside of the surface, and $f(x) < 0$ inside of the surface of an object in question, where the value at any given point is the closest distance to the surface. The gradient thus gives the surface normal.
#### Occupancy Networks
You simply learn a function which, as a function of space, determines whether the space is free or occupied. Tesla uses this for self driving cars (rather than ontological descriptions of "what" is located in different places).
#### Deformation Fields
$d(x) \in \mathbb{R}^3$ which maps points from one configuration to another, to simulate non-rigid motion.
### Object Centric Factorization
You use segmentation to localize different objects in space.

## Illustrative Experiment: Dot position on circle
Suppose we have the following data: a white circle on a black background. A red dot is on the circle, at a specific angle. Our goal is to train a model that computes the angle of the circle off of the X-axis.
![[Screenshot2026-01-22_17-10-14.png]]
e.g. $\theta \approx -\frac{\pi}{4}$

Now, if we apply the transformation $\phi(\theta \cdot 64 / 2\pi, r) = (\sqrt{(x - c_{x})^2 + (y - c_{x})^2},  \arctan{(y - c_{y})/(x - c_{x})})$ that is, which converts the image into polar co-ordinates, we get the following image:
![[Pasted image 20260122171616.png]]

In this form, we observe the nice property that the position of the red dot in the image along the $x$-axis is now proportional to the angle $\theta$... we could even technically say that it is translation invariant. The idea is, that CNNs are translation equivariant within the grid. By converting to polar co-ordinates, we are mapping to a space which is translation equivariant w.r.t. to the $\theta$ parameter.

Now, we train two small CNNs, and compare their performance at identifiying the original $\theta$ value. Both models are of the same type. The input are these 64 x 64 pixel images. 1000 images were generated, with 800 test images and 200 validation images.

![[Screenshot2026-01-22_17-35-26.png]]

![[Pasted image 20260122173506.png]]

![[Pasted image 20260122173313.png]]
# Mathematical Formulation
In this section, I will try and formalize the mathematical expression of these ideas, specifically in the context of reinforcement learning.
## Symmetry-Preserving MDP Homomorphisms
Let $\mathcal{M} = (\mathcal{S}, \mathcal{A}, P, r, \mu_{0})$ be a Markov Decision Process (MDP).
Then, let $\bar{\mathcal{M}} = (\bar{\mathcal{S}}, \mathcal{A}, \bar{P}, \bar{r}, \bar{\mu}_{0})$ be an MDP for which there exists a state space homomorphism $\phi : \mathcal{S} \to \bar{S}$ such that for each $\bar{s}, \bar{s}' \in \bar{S}$,

$$
\bar{P}(\bar{s}' | \bar{s}, a) = \sum_{s' \in \phi^{-1}(\bar{s}')} P(s' | s, a)
$$
and
$$
\sum_{s' \in \phi^{-1}(\bar{s}')} P(s' | s_{1}, a) = \sum_{s' \in \phi^{-1}(\bar{s}')} P(s' | s_{2}, a), \quad \forall s_{1}, s_{2} \in \phi^{-1}(\bar{s})
$$
(this condition ensures that the map $\phi$ behaves properly as a homomorphism of an MDP, and properly determines equivalences between states in $S$, in the range $\bar{S}$),
$$
\bar{r}(\bar{s}, a) = r(s, a), \quad \forall s \text{ s.t. } \phi(s) = \bar{s}
$$
Let $G$ be a group, and suppose $\rho: G \to \text{Aut}(\mathcal{S})$ is a group action on the state space. In particular, this might not be a linear representation... the representation could be very complicated. For example, if our group action in reality are translations in $SE(3)$, but our state space are camera images of our scene, then translations/rotations of the objects in our scene will result in complicated function relating movement of pixels in images.
Suppose also that we have some group action $\rho_{\mathcal{A}} : G \to \text{Aut}(\mathcal{A})$  such that these group actions respect the $MDP$ structure, that 
$$
P(\rho(g)s' | \rho(g)s, \rho_{\mathcal{A}}(g)a) = P(s' | s, a) \quad \forall g \in G
$$
and
$$
r(\rho(g)s, \rho_{\mathcal{A}}(g)a) = r(s, a) \quad \forall g \in G,
$$
and also that the map $\phi$'s fibers are respected, that
$$
\phi(s_{1}) = \phi(s_{2}) \implies \phi(\rho(g)s_{1}) = \phi(\rho(g)s_{2})
$$
Then, we can induce a group action on $\bar{\mathcal{M}}$ by using the group action on $\mathcal{M}$  through the map $\phi$:
$$
\bar{\rho} : G \to \text{Aut}(\bar{\mathcal{S}})
$$
$$
\bar{\rho}(\bar{s}) = \rho(s) \quad \text{ for any } s \in \phi^{-1}(\bar{s})
$$
and we can prove that this map is well defined.

In particular, $\bar{\mathcal{M}}$ can be a state space where the induced group action $\bar{\rho}$ behaves nicely and is easy and convenient to work with. For example, it might be linear. That is, we could have $\bar{\rho} \in GL(V)$, even if the image of $\rho$ in $\text{Aut}(S)$ might be very complicated.
## Equivariance and Sample Efficiency
Now, we ask the fundamental question: even if a symmetry exists in our state space (that respects the MDP), how can we determine which group actions are helpful in terms of gaining sample efficiency when learning?

Let $(\mathcal{M}, G, \rho)$ be an MDP with a group and group action which respects its structure.
Let $\mathcal{X} = \mathcal{S} \times \mathcal{A}$
For $(s,a) \in \mathcal{X}$, define its *orbit*:
$$
\mathrm{Orb}_G(s,a)
\;=\;
\{\rho_{\mathcal{S}}(g)s,\rho_{\mathcal{A}}(g)a) \mid g \in G\} \subseteq \mathcal{X}.
$$
Similarly, we can define the orbit of a state $s \in S$ as
$$
\text{Orb}_{G}(s) = \{ \rho_{S}(g)s | g \in G \} \subseteq S
$$
Intuitively speaking, this is the set of elements that are "connected" via the equivariance. A policy that is equivariant w.r.t. these group representations will be such that state $(s, a)$ will inform $(\rho_{S}(g)s, \rho_{A}(g)a)$ for every $g \in G$, and vice versa.

Now, suppose we have a policy $\pi : S \times A \to A$ and a set of trajectories collected with $\pi$, $\{ (s_{0, i}, a_{0, i}, \dots, s_{N_{i}, i}, a_{N_{i, i}}) \}_{i=1}^N$ where the initial states are sampled by $s_{0} \sim \mu_{0}$.
Then, consider the multiset of states, $\mathcal{D} = \{ s_{i}\}_{i}$ visited in our trajectories.
Now, define:
$$
d_{G}(s_{i}, s_{j}) = \inf_{g \in G} \lvert s_{i} - \rho(g) s_{j} \rvert.
$$
Then, if $d_{G}(s_{i}, s_{j})$ is small, and our policy has some for of continuity constraint, we can infer that any inference performed on state $s_{j}$ which improves the policy's choice of action on that state will also benefit $s_{i}$, so long as the symmetry respects $\mathcal{M}$.
Intuitively, we can predict that if the measure $\mu(\{\mathcal{D} \cap \text{Orb}_{G}(s_{i})  \})$ is larger, then we might suppose that a $G$-equivariant policy will have significantly greater sample efficiency in determining a correct policy for $s_{i}$ than a non-equivariant policy. 

In particular, if $G$ and $H$ are two groups with representations on symmetries that respect our space, it could be the case that $\sum_{i}\mu(\{ \mathcal{D} \cap \text{Orb}_{G}(s_{i}) \}) \geq \sum_{i} \mu(\{  \mathcal{D} \cap \text{Orb}_{H}(s_{i}) \})$, in which case we might come to the conclusion that applying $G$-equivariant policies is more fruitful than applying $H$-equivariant policies.
## Sample Efficiency of Group-Equivariant Homomorphisms
Next, we consider the case when we have a state space homomorphism $\phi : S \to \bar{S}$ which respects the fibers of the homomorphism. In that case, we might have that even if $\mu(\{ \mathcal{D} \cap \text{Orb}_{G}(s_{i}) \})$ is small, $\mu(\{ \phi(\mathcal{D}) \cap \text{Orb}_{G}(\phi(s_{i})) \})$ is significantly larger. Indeed, consider that $\text{Orb}_{G}(s_{i}) \subseteq \phi^{-1}(\text{Orb}_{G}(\phi(s_{i}))$, but it could very well be the case that $\phi^{-1}(\text{Orb}_{G}(\phi(s_{i})) \not\subseteq \text{Orb}_{G}(s_{i})$, especially if $\ker \phi(S)$ is a "nuisance group" (pose, viewpoint, background objects) which may not be in the kernel of the group action $\rho_{S}$.
In that sense, we can potentially compare different state space homomorphisms according to how well they meaningfully group together equivalent states into fibers of states in $\bar{\mathcal{M}}$ to increase the sample efficiency of a policy learning from collected state action pairs in $\mathcal{D}$.
## Potential Definitions for Group Sample Efficiency Measure 
Recall that the objective is, to find a measure which is quick to compute that will let you know if a specific group equivariance is a good inductive bias on a given dataset in order to increase sample efficiency.
$$
\frac{1}{|X|} \sum_i \frac{1}{|G|} \sum_{g \in G} \text{NNdist}(g \cdot x_i, X)
$$
Expressions for $\mathcal{M}_{haar}$ and $\mathcal{M}_{occ}$
Let $X = \{x_i\}_{i=1}^N$ be our dataset.
Let (g) be a group element (SO(2) rotation, or SE(2) rotation+translation).
Let $\mathrm{NNdist}(y, X) = \min_j |x_j - y|$.

$\mathcal{M}_{haar}$ (uniform group sampling)
$$
\mathcal{M}_{\text{haar}} = \frac{1}{N} \sum_{i=1}^N \frac{1}{|G|} \sum_{g \in G_{\text{uniform}}} \mathrm{NNdist}(g \cdot x_i,; X)
$$

Where $G_{\text{uniform}}$ is a uniform discretization of SO(2):
$$
\theta_k = \frac{2\pi k}{K}, \quad k=0,\ldots,K-1
$$
### Summary
Experiments to illustrate the principle:
- Some 2D point-goal navigation with obstacles. Observation is egocentric RGB. BEV occupancy/costmap.
- RGB cameras, with multi-view images, from an angle, possible occluded by robot. Map to object-centric pose (x, y, theta, x_g, y_g, theta_g), and apply an equivariant network. Compare to canonicalization (applying rotation directly to co-ordinates).
- Something to do with multi-agent objects, where permutation symmetry is clear.

# February 2, 2026

## Summary
Today, we 
- Zero-d in on the specific end of our measure: to determine the usefulness of a specific representation in uncovering underlying symmetry and gaining sample efficiency with an equivariant network.
- Determined that we do not want to work with the occupancy measures of the optimal policy... we want to work with state action pairs generated by weak or random policies.
- Came up with some basic measures to test, and implemented them in the reacher prototype. See the python file in VSCode.

Experiments to illustrate the principle:
- Some 2D point-goal navigation with obstacles. Observation is egocentric RGB. BEV occupancy/costmap.
- RGB cameras, with multi-view images, from an angle, possible occluded by robot. Map to object-centric pose (x, y, theta, x_g, y_g, theta_g), and apply an equivariant network. Compare to canonicalization (applying rotation directly to co-ordinates).
- Something to do with multi-agent objects, where permutation symmetry is clear

| Symmetry exists | Coverage exists | Representation exposes | Equivariance helps? |
| --------------- | --------------- | ---------------------- | ------------------- |
| yes             | yes             | yes                    | ✔                   |
| yes             | no              | yes                    | ✘                   |
| yes             | yes             | no                     | ✘                   |
| yes             | no              | no                     | ✘                   |
# Cyrus Meeting Notes February 3, 2026
### Main Points In Meeting
- Can we use this measure in order to learn a representation into a feature space such that equivariance is helpful?
- Can we relate this easily computable equivariance measure to theoretical concepts in statistical learning, to get real theoretical results instead of just something empirical?
- What experiments can we run in order to prove that this metric works?
### Follow Up Questions
- What does it mean for the metric to work?

# February 16, 2026
I have read through the ChatGPT and Deep Research comments on my notes carefully. Here are my reflections.
- Instead of trying to prove something about absolute error bounds, try and prove something about the relative performance of an equivariant network (in this case, once we have a certain metric on our data) to a non-equivariant network
	- Look into VC dimension proofs, covering number, Rademacher complexity.
- Learning MDP homomorphisms is difficult, and must be done in conjunction with policy learning (see policy gradient state abstraction paper)
	- Look into bi-simulation metrics more carefully, and especially in the context of symmetry breaking.
- Show that your metric demonstrates well empirically when an equivariant NN will outperform a non-equivariant NN.
	- Have 3 or 4 different representations for a single environment. Then, rank them based on sample efficiency performance, and also the metric. Show that the metric is a good predictor.
		- Do so for a heavier robotics environment and a lighter toy (such as reacher) environment. (The heavier environment will need to be engineered; do your best to code it up).
	- Finally, try and learn correct homomorphisms, using the metric as a loss function.

## List of Papers and References Acquired through the readings
### Learning MDP Homomorphisms and latent equivariant spaces
- [[2024_panangaden_LearnMDPHomomorphisms| Here]], we develop policy gradient learning through abstract spaces. They learn the abstract space at the same time as the policy which solves the MDP, with the goal being using the abstract space (MDP homomorphism) to increase sample efficiency.
- [[2019_Biza_AbstractMDPHomomorphismWithDeepLearning|In contrast]], this paper learns an MDP homomorphism strictly from states.
- [[2022_Park_LearningSymmetryEmbeddingsEquivariantWorldModels|This paper ]] somehow learns embeddings that are helpful for learning representations... how it works, I'm not sure.
- [[2022_Mondal_EquivariantRepresentationsForDataEfficientRL |Here, we]] learn the equivariant representation.
### Canonicalization
- [[2024_Dym_EquivariantCanonicalizationProblems|This paper]] shows us problems we face when we try to canonicalize group elements.
### Theoretical Papers on Sample Efficiency and Generalization
- [[2023_SichengZhu_DLSymmetryGeneralizationBenefit| Important paper]] on understanding the sample efficiency of equivariant models.
- [[2023_Tahmasebi_GainFromSymmetryForKernelRegression| Theoretical paper]] which considers the case of kernel ridge regression and the gains you get from smooth group actions on manifolds. First, read up on kernel ridge regressions to try and understand this.
- [[2020_Chen_GroupTheoryFrameworkForDataAugmentation| Data Augmentation]] has a theoretical foundation, and this paper supposedly supplies algorithms to measure this.
- [[2021_Elesedy_ProvableGeneralisationBenefitEquivariantModels|Mathier]] paper on equivariance generalization benefit.
- [[2024_Perin_DLAbilityToLearnSymmetries|Paper on]] whether or not Deep Networks can learn symmetries from data. 


# February 23, 2026
## Experiment Outline
### Background and Setup
The goal of this work today is to test what the average distance $\alpha$ between a dataset and the orbits of its points has to say about the effectiveness of different state space representations for a basic RL task. To do so, I will implement a class which computes $\alpha$ for different state space representations for the same task, where each state space representation comes with a corresponding group action, for perhaps different groups for each state space representation. Then, I will compute small (low parameter) equivariant Deep RL algorithms for each of these state spaces where the symmetries are respected, along with non-equivariant models of comparable size. Then, I will directly compare the measure $\alpha$ with the benefit equivariant models have over non-equivariant models. I aim to do this with different initial state distributions. 
### Hypothesis
If the initial state distribution is evenly distributed over the orbits of the states, so that $\alpha$ is small, then the sample efficiency gain of the equivariant network will be greatest, and the equivariant networks will significantly outperform the non-equivariant ones. However, if the initial distribution of the states is narrow, and the orbit strays far from the initial dataset, then the sample efficiency gain of the equivariant network will be smaller, and we will see similar performance between the two of them.
## Code Development
To that end
- Start with a circle, until you get all your data processing/orbit distance algorithm right. Compute this measure for different distributions of the circle.

Implement the following class
- Stores data-points (in euclidean space, or perhaps images, depending on what your data is), in some sort of datatype.
- Implements some metric between the data-points (depends on what the data is... perhaps leave this as an abstract method)
- In the initialization, takes some group object from ESCNN package.
- Then, has a method to compute all the points in the orbit of a group.
- Implement two methods
	- One takes a point. For every point in the orbit of that point, it computes the nearest neighbor in the dataset. It then, computes the distance to that neighbor. Finally, it returns the average of all these distances, that is, the points in the orbit.
	- One computes the above metric for every point in the dataset, and takes the average of those values.

### Phase 1: Haar Measure
In order to test this class, try the following
- Randomly generate data points on a circle, where each point is parameterized by $\theta \in [0, 2\pi)$, and you generate the points according to the distribution $p(\theta)$.
- Compute the above metric, with the euclidean distance, for the following distributions: Bump Function, Uniform Distribution, etc.

Next, set up the Mujoco reacher environment. Compute random starting positions, for 100 or so locations.
- Compute states which measure the relative distance between the end effector and the goal, and store a dataset. Measure Euclidean distance. (SE2)
- Compute states which measure both the position of the end effector and the goal, relative to the origin, and store a dataset. Measure mean of the two euclidean distances of these two vectors. (SO2)
- Capture images of starting states, and store a dataset with these images. Do some reasonable measure of distance between images. (Discretized SO2,  probably D8)
- Translation group: subtract end effector from goal. In this case, measure euclidean distance to nearest other point (translation group already applied, simply measure the distance to the nearest neighbor). (T2)
Compute the measures for each of these.
Next, subclass reacher environment and override reset model. Create a custom initial distribution, which spawns the end effector and the goal within a specific section of the orbit of the symmetry group each reset. Then, re-run the same random starting positions. Compute the measure for each of the 4 state spaces.

### Phase 2: RL
Implement an RL algorithm
- SAC
- 100K trials
I worked out how to implement the action space equivariance for each of the representations:
1. Image case (D8)
    - Use a D8-equivariant encoder.
    - Use an action head with a **flip-swap representation**:
        - Rotations act trivially (invariant).
        - Reflection swaps two action channels.
    - That is a valid group action (a permutation rep induced by the reflection subgroup C2 inside D8).
2. SO(2) case
    - Invariant action head is fine.
3. SE(2) and T(2) cases

- Define policy action as desired EE acceleration in workspace: a_des in R^2.
- Group action on action:
    - Rotation: a_des -> R a_des
    - Translation: unchanged
- Then use a low-level controller to map a_des to torques (quick operational-space controller, damped pseudoinverse/Jacobian-based).  
    This gives a consistent equivariant action transformation.

### ChatGPT Comments
- Use SSIM for image distances, tentatively. Metric choice is difficult, and not always practical.
#### Group equivariance


Finally, for each of these 4 state spaces, implement an RL algorithm. Use the ESCNN package to implement an equivariant algorithm (discrete D8 or D16 for SO2, SE3, SO2... no data augmentation) and a non-equivariant RL algorithm of similar size.

For the output, graph reward vs trials for each of these 8 algorithms/state spaces, with the equivariant and non-equivariant model on a single graph. Label the sample efficiency measure $\alpha$  on the title of the graph as well.

## Results
### Phase 1
- Problem: orbit was poorly covered, but $\alpha$ still came out low simply because the vectors were small... change metric to be normalized with respect to the size of the vector of which the orbit is being taken.
- Had to make sure that the secondary distribution of the initial conditions that aims to illustrate when orbit coverage is low actually has low orbit coverage.
	- At first, I restricted the EE and goal position to be in the first quadrant. But this actually increased orbit coverage for SE2, because of the way it restricted the possible size of the vectors (so more of them were within the same orbit... size is the only thing that changes which orbit you are in).
	- Then, I came to my senses, and restricted the angle of the vector $EE - \text{Goal}$. This then gave the expected results.
	- Finally, for SO2 (since this configuration contains two vectors) I considered the setup where we keep the goal state within some small angle off of the origin.