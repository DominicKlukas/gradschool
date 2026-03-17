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


In this section, I will try and formalize the mathematical expression of these ideas, specifically in the context of reinforcement learning.
# Mathematical Formulation
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
\mathcal{M}_{\text{haar}} = \frac{1}{N} \sum_{i=1}^N ; \frac{1}{|G|} \sum_{g \in G_{\text{uniform}}} \mathrm{NNdist}(g \cdot x_i, X)
$$

Where $G_{\text{uniform}}$ is a uniform discretization of SO(2):
$$
\theta_k = \frac{2\pi k}{K}, \quad k=0,\ldots,K-1
$$

$\mathcal{M}_{occ}$ (occupancy‑weighted sampling)
Let $p(\theta)$ be the empirical angle distribution from the data, computed from the canonicalization.
$$
\mathcal{M}_{\text{occ}} = \frac{1}{N} \sum_{i=1}^N \; \frac{1}{K} \sum_{g \sim p(\theta)} \mathrm{NNdist}(g \cdot x_i,; X)
$$
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

## Deep Think's Response
The measure you have developed is effectively an estimator of the **"Symmetry Gap"** or **"Orbit Expansion."** It measures the volume of the state space that is reachable via symmetry but is currently unexplored by your training data. 
- [COMMENT] 
	- No it isn't. It measures how much equivariance will help you given a specific MDP (since equivariance will help your MDP if the states your MDP sees for the policies you use cover the orbits of your groups relatively nicely).
Here is a brainstorming of formal mathematical links between your specific Haar measure ($\mathcal{M}_{\text{haar}}$) and "learning improvement," structured for your paper.  
### Effective Sample Size
The "Effective Sample Size" Multiplier (Sample Efficiency)  
This is the most direct link to data efficiency. You can argue that an equivariant network effectively "hallucinates" valid data points in the gaps identified by your measure. 
- [COMMENT]
	- But if you never actually see those "valid points", then it will not result in any sample efficiency gains. In the RL case, the same $\mu_{0}$ that is present in your training data is there in your validation dataset, and when you are using your policy.
	- This is not the case when you are considering imitation learning: you might have a specific set of trajectories that you are trying to imitate. Then, the training dataset might cover a small part of the "orbits" of the group action.
		- In this case, we are interested in the set of trajectories or states that we see in the "useful life" of the policy, during validation.
**The Formal Metric:**  
You must normalize your measure by the local density of the dataset to make it unitless and comparable across representations. Let $\delta_{\text{data}}$ be the average nearest-neighbor distance within your dataset $X$ (the "resolution" of your data).  
- [COMMENT]
	- This is a good idea.
Define the **Symmetry Expansion Ratio ($\gamma$)**:  
$$\gamma(\phi) = \frac{\mathcal{M}_{\text{haar}}(\phi)}{\delta_{\text{data}}(\phi)}$$  
**The Hypothesis:**  
The **Effective Sample Size ($N_{\text{eff}}$)** of an equivariant network scales with this ratio:  
$$N_{\text{eff}} \approx N \cdot (1 + \gamma(\phi))$$  

- **If $\gamma \approx 0$:** The orbits collapse onto existing data (the dataset is already dense/symmetric). Equivariance adds no new information. **Gain: Low.**
- **If $\gamma \gg 1$:** The orbits sweep through empty space. The equivariant network generalizes to these regions for free, while a standard network treats them as unknown. **Gain: High.**
- [COMMENT]
	- This is wrong. See above comments.

**Experimental Prediction:**  
In `Reacher-V5`, if you plot the **Relative Sample Efficiency** (samples needed for Standard / samples needed for Equivariant) against $\gamma$, you should see a linear or super-linear correlation.  
- [IDEA]
	- The point is, $\gamma$ is a measure of how much better equivariant policies will be from learning from a dataset than a non-equivariant policy. If all the different samples are contributing to different "orbits", then sure, more spaces are covered, but the same amount of learning has been done, and if non of the other points in those orbits are ever used, it is not useful for your dataset. The point is, that the distribution of your training dataset typically should be sampled from the same distribution as your validation set/production data.
	- I don't know if this will be true... in some sense, $\mathcal{M}_{haar}$ is a measure of the density of the dataset... in this sense, normalization is very important, because it factors out the density. However, our dataset might still be pretty sparse, but it could be that points are paired up so that they have close neighbors. So finding the right way to normalize (average nearest neighbor, average distance to other points, etc) might be something to consider.
### Lipschitz Generalization Bound
This links your measure directly to the generalization error (test loss).  
#### The Theory:  
Standard neural networks are Lipschitz continuous functions ($f$). The error on a test point $x_{\text{test}}$ is bounded by the error on its nearest training neighbor $x_{\text{train}}$:  
$$|f(x_{\text{test}}) - y| \le |f(x_{\text{train}}) - y| + L \cdot \|x_{\text{test}} - x_{\text{train}}\|$$  
If the target function is truly equivariant, an equivariant network effectively "moves" $x_{\text{test}}$ along its orbit to find a closer match.  
#### The Formal Link:
Your measure $\mathcal{M}_{\text{haar}}$ is literally the expected value of the distance term $\|x_{\text{test}} - x_{\text{train}}\|$ that is eliminated by equivariance.  
$$\text{Expected Error Reduction} \propto L \cdot \mathcal{M}_{\text{haar}}$$
- [COMMENT]
	- Here, expected error reduction means the expected error reduction we will gain when we use an equivariant policy vs a non-equivariant policy. 
You can frame $\mathcal{M}_{\text{haar}}$ as a proxy for the **"Geometric Generalization Risk"**. A high value means a standard network is forced to extrapolate into voids, while an equivariant network effectively interpolates.
- [COMMENT]
	- Gemini's incorrect understanding.
### Intrinsic Dimension Reduction (Manifold Learning)  
This addresses your interest in the "dimension of the data manifold."  
The Idea:
- **Standard Net:** Learns on the full data manifold $\mathcal{S}$. Dimension $d$.
- **Equivariant Net:** Learns on the quotient manifold $\mathcal{S}/G$ (the manifold of orbits). Dimension $d - \dim(G)$.

**The Formal Metric:**  
You can estimate the **Dimensionality Gap ($\Delta_{\text{dim}}$)**.  
Use a standard intrinsic dimension estimator (like Levina-Bickel) to measure the dimension of the raw data ($d_{\text{raw}}$).  
Then, measure the dimension using your **Orbit Distance** metric ($d_{\text{orbit}}$), where distance is $D(x,y) = \min_g \|x - g \cdot y\|$.  
$$\Delta_{\text{dim}} = d_{\text{raw}} - d_{\text{orbit}}$$  
- [COMMENT]
	- I think the idea here, is that dimension is computed using some metric. If we use the orbit distance metric, then we will get a smaller measure for dimension than if we use the raw point metric.
**The Hypothesis:**  
Since sample complexity often scales exponentially with dimension ($N \propto e^d$), a representation $\phi$ that maximizes $\Delta_{\text{dim}}$ (by successfully collapsing the symmetry orbits) will yield exponential gains in efficiency.  
- [COMMENT]
	- Yes, this seems correct to me. Note how, if $\gamma$ is big, then the metric will still be large, and so it will not reduce the dimension of our orbits.
	- This seems like an interesting measure, if there are meaningful theoretical results for me to apply this to. 
Critical Nuance: The "Policy Consistency" Check  
In RL, a representation can be geometrically equivariant (High $\mathcal{M}_{\text{haar}}$), but the optimal policy might _break_ that symmetry (e.g., gravity makes "up" special).  
To ensure your measure predicts _useful_ learning improvement, you should add a consistency term.  
**The "Symmetry-Task Compatibility" Score:**  
$$\mathcal{S}_{\text{task}} = \underbrace{\frac{\mathcal{M}_{\text{haar}}}{\delta_{\text{data}}}}_{\text{Novelty (Good)}} - \lambda \cdot \underbrace{\mathbb{E} \left[ \| \rho_{\mathcal{A}}(g)\pi^*(x) - \pi^*(g \cdot x) \| \right]}_{\text{Symmetry Breaking (Bad)}}$$  
- [COMMENT] Indeed, so far we only measured the orbits of the states (measuring the orbits of the state-action pairs will be more sparse, which was my worry), but measuring symmetry breaking is definitely another thing to compute.
[Question]
- Given that "simple to compute" is in the sales pitch (I could envision this being something we might want to compute during validation runs), don't we have to worry about the algorithmic complexity of this measure? How can we reduce this?

Proposed Experiment for Reacher-V5  
To validate this in your paper, run a **Correlation Study**:  
1. **Input:** Define 3 representations (e.g., Cartesian, Polar, Random Projection).  
2. **Measure:** Calculate the **Symmetry Expansion Ratio ($\gamma$)** for each on a fixed, small random dataset.  
3. **Train:** Train both Standard and Equivariant agents to convergence.  
4. **Plot:**  
**X-Axis:** The Ratio $\gamma$ (calculated _before_ training).  
**Y-Axis:** The Speedup Factor ($\frac{\text{Steps}_{\text{Standard}}}{\text{Steps}_{\text{Equivariant}}}$).  
**Prediction:** You will see a strong positive correlation, proving that your metric $\mathcal{M}_{\text{haar}}$ is a valid predictor of "Equivariant Advantage."
- [COMMENT] This is the obvious intuitive way to run an experiment to test this.

## Gemini Standard Response
This is a fascinating direction. You are effectively trying to quantify the **"information gain" of a symmetry group** with respect to a specific dataset.  
The intuition you are building is correct: if the orbits of your group action (OrbG​(s,a)) land in regions of the state space that are currently _empty_ (high distance from existing data), enforcing equivariance allows the model to "conquer" those regions for free. If the orbits land right on top of existing data, the symmetry is already implicitly covered, and the gain is marginal.  
- [COMMENT] Wrong, as discussed.
Here is a formal mathematical framework to link your Haar measure metric to learning improvement, specifically **Sample Complexity** and **Manifold Covering**.   
1. The Formal Link: Quotient Space Covering Numbers  
The formal notion you are looking for is the reduction in the **Covering Number** of the hypothesis space.  
• **The Theory:** Learning bounds (generalization error) are typically proportional to NlogN(ϵ,X)​​, where N is the covering number (how many balls of size ϵ are needed to cover the data manifold X) and N is the number of samples.  
- [QUESTION] how does this integrate with current theory on how deep learning works so well? Is this a general statistical idea, with deep theorems that still hold in the case of deep learning?
• **The Equivariant Gain:** When you enforce G-equivariance, you are effectively learning on the **Quotient Space** X/G (the space of orbits) rather than X.  
• **The Improvement:** The learning improvement comes from the ratio of the covering numbers:  
Gain≈Vol(X/G) : Vol(X)​≈∣G∣  
(For finite groups. For continuous groups, this relates to the dimension reduction of the manifold).  
Your metric is an empirical estimator of this "Gain". It measures how effectively the group action G _fills the gaps_ in the current ϵ-cover of your dataset.  

  Goal of paper:
> "We propose that the effectiveness of an equivariant inductive bias is determined by the **Orbit Expansion Ratio (γ)** of the representation. We hypothesize that equivariance improves sample efficiency if and only if the group action maps observed states to valid, low-density regions of the latent manifold (High γ), effectively reducing the covering number of the state space."



# February 12, 2026
After reading through the Gemini notes carefully, I gave my comments. Then, I pasted these notes into Gemini DeepThink, ChatGPT Research Mode, and ChatGPT standard. I have the queries pasted below.
## ChatGPT Deep Research: Measuring when representation changes expose useful symmetries for sample-efficient robotics RL
### Problem framing: representation as symmetry “unmasking”
Your core setup—start from an observation space with messy, non-linear induced transformations, then map into a representation where a group action is “simple” enough to exploit—is already a well-trodden motif across vision, robotics, and equivariant learning, but with an important twist: you want a _predictive, cheap-to-evaluate_ criterion for when a given representation/operator family will actually translate into _sample-efficiency gains_ in an RL/robotics loop.
Several robotics/vision papers can be read explicitly as “representation changes that make a symmetry easy”:
- **Bird’s-eye-view lifting** converts camera imagery into a top-down raster where planar translations/rotations correspond to near-rigid motions on a grid, aligning with standard convolutional inductive biases (and enabling downstream planning on a BEV cost map).
    - Lift, Splat, Shoot (Philion & Fidler, 2020): [https://arxiv.org/abs/2008.05711](https://arxiv.org/abs/2008.05711)
- **Ray-based representations** reinterpret RGB inputs as a set of rays that transform naturally under 3D roto-translations, enabling SE(3)-equivariant structure _without_ requiring depth/point clouds as input.
    - RAVEN: End-to-end Equivariant Robot Learning with RGB Cameras (Klee et al., 2026): [https://openreview.net/forum?id=b90f264ff3216c591bf2ed4ce88eae7b9745f7ab](https://openreview.net/forum?id=b90f264ff3216c591bf2ed4ce88eae7b9745f7ab)
- **Polar/log-polar reparameterizations** explicitly turn rotations (and sometimes scalings) into translations in a canonical coordinate system, so “translation equivariance” becomes “rotation/scale equivariance” after a warp—very close in spirit to your dot-on-circle example.
    - Polar Transformer Networks (Esteves et al., 2018): [https://arxiv.org/abs/1709.01889](https://arxiv.org/abs/1709.01889)
This perspective also shows up in the more formal RL abstraction literature: MDP homomorphisms and symmetry reduction are exactly about _collapsing redundant structure_ so you solve a smaller/easier problem while preserving decision-relevant behavior.
- Ravindran, B. (2004). _An Algebraic Approach to Abstraction in Reinforcement Learning_ (UMass Amherst PhD thesis).
The research question you wrote (paraphrased): _which representation changes expose underlying group structure in a way that can be exploited, and can we predict the resulting sample-efficiency lift from data collected by weak policies?_—is aligned with a data-centric generalization theory thread in invariance learning that introduces computable “dataset + transformation” metrics:
- Zhu, An, Huang (NeurIPS 2021), “Understanding the Generalization Benefit of Model Invariance from a Data Perspective”: [https://proceedings.neurips.cc/paper/2021/hash/2287c6b8641dd2d21ab050eb9ff795f3-Abstract.html](https://proceedings.neurips.cc/paper/2021/hash/2287c6b8641dd2d21ab050eb9ff795f3-Abstract.html)  
    (arXiv version: [https://arxiv.org/abs/2106.12052](https://arxiv.org/abs/2106.12052))
### When equivariance helps sample efficiency in RL: what must be true
Your table (“symmetry exists / coverage exists / representation exposes”) is the right decomposition, and it can be sharpened into three necessary-ish conditions that show up repeatedly across theory and robotics practice.
**(1) The MDP must be symmetric (or approximately symmetric) with respect to the chosen group action** in reward and transitions. This is the classical “symmetry in MDPs” viewpoint and also the basis for homomorphism-based reduction. 
- [MDP Homomorphic Networks: Group Symmetries in RL](https://proceedings.neurips.cc/paper/2020/file/2be5f9c2e3620eb73c2972d7552b6cb5-Paper.pdf)
**(2) The target you’re learning must actually respect the symmetry you impose** (or be close enough). In supervised learning, this is “the Bayes/target function is invariant/equivariant”; in RL it is more subtle (Q*, π*, model dynamics). Your warning (“gravity makes up special”) is the real failure mode: enforcing the wrong symmetry can hurt.
- [Equivariant Frames and the Impossibility of Continuous Canonicalization](https://proceedings.mlr.press/v235/dym24a.html)
**(3) The data distribution encountered during learning/evaluation must make symmetry constraints useful.**  
The right intuition is: invariance helps when it reduces the effective complexity of the learning problem _relative to the data you see_. “Useful” does **not** mean “the orbit visits totally unseen regions,” but rather “the invariance meaningfully reduces degrees of freedom needed to generalize on the rollout/test distribution.”
- **Transformation-induced sample covers** and a statistic you can empirically evaluate to guide transformation selection:
	- [Understanding the Generalization Benefit of Model Invariance from a Data Perspective](https://arxiv.org/pdf/2111.05529)
- **Quotient-space / exact sample complexity gain** (clean theory sandbox: kernels on manifolds under Lie group actions):
	- [The Exact Sample Complexity Gain from Invariances for Kernel Regression](https://proceedings.neurips.cc/paper_files/paper/2023/file/adf5a38a2e2e7606fbfc3eff72998afa-Paper-Conference.pdf)
- **Group augmentation as orbit averaging / variance reduction** (precise version of the “augmentation helps” story):
	- [Group Equivariant Convolutional Networks](https://proceedings.mlr.press/v48/cohenc16.pdf)
### Your orbit-distance measure: what it’s estimating, when it fails, and how to repair it
#### Your critique of “orbit expansion = free improvement” is right
The claim “if orbits land in empty space, equivariance conquers those regions for free” is not generally valid in RL unless those orbit-shifted states matter under the rollout/evaluation distribution and symmetry assumptions.
A more defensible interpretation of  
$$  
\mathcal{M}(\phi,G)\approx \mathbb{E}_{x\sim \text{data}};\mathbb{E}_{g\sim p(g)}\Big[\mathrm{NNdist}\big(g\cdot x,;X\big)\Big]  
$$
is that it estimates a **data-induced recoverability / sample-cover property under transformations**, not “free exploration of orbit volume.” This lines up closely with the transformation-induced sample cover viewpoint:
- Zhu, An, Huang (NeurIPS 2021): https://arxiv.org/abs/2111.05529 
#### Key failure mode: orbit size vs generalization benefit
Large orbit excursions (big NN distances after applying random g) can mean:
1. **The group is invalid for the task** (symmetry breaking) → enforcing it harms.
2. **The representation does not expose/linearize the group action** → “g·x” is not semantic equivalence.
3. **The occupancy distribution has low orbit coverage** under the policy used to generate X → valid but rare/unvisited.
This is why exact overlap / strict cover-number arguments need approximate/Lipschitz refinements rather than exact orbit duplicates:
- Zhu, An, Huang (NeurIPS 2021):https://arxiv.org/abs/2111.05529
#### A repaired version that matches your table
To match your “symmetry exists / coverage exists / representation exposes” logic, separate:
**A. Symmetry validity / task-compatibility**  
Estimate whether the environment is approximately G-equivariant in one-step transitions and rewards. In simulation you can often implement world transforms directly to test this.
(You can cite Ravindran & Barto for the homomorphism/symmetry framing.)
- Ravindran & Barto (2004): [https://people.eecs.berkeley.edu/~pabbeel/cs287-fa09/readings/ravindran_barto_2004.pdf](https://people.eecs.berkeley.edu/~pabbeel/cs287-fa09/readings/ravindran_barto_2004.pdf)
**B. Coverage under the relevant occupancy distribution**  
Prefer occupancy-weighted g sampling (your idea of ( \mathcal{}_{occ} )) over Haar-uniform g when you want prediction of _real rollout benefit_.
**C. Representation exposure**  
Measure whether there exists a stable/simple induced action (\bar\rho(g)) such that  
$$
\phi(\rho(g)x)\approx \bar\rho(g)\phi(x)  
$$ 
(You can connect this to the literature on equivariance construction / canonicalization.)
- Finzi et al. (2021): [https://arxiv.org/abs/2104.05818](https://arxiv.org/abs/2104.05818)
- Cohen & Welling (2016): [https://proceedings.mlr.press/v48/cohenc16.html](https://proceedings.mlr.press/v48/cohenc16.html)
### Complexity: yes — standard reductions
Your complexity concern is real; naïvely computing NNdist over many g values is expensive. Standard accelerations:
- **Approximate nearest neighbor indexing** (HNSW):
    - Malkov & Yashunin (TPAMI 2020): [https://arxiv.org/abs/1603.09320](https://arxiv.org/abs/1603.09320)
- **GPU-accelerated similarity search** (Faiss):
    - Johnson, Douze, Jégou (2017): [https://arxiv.org/abs/1702.08734](https://arxiv.org/abs/1702.08734)
- **Stochastic estimation** (subsample x’s and g’s, compute kNN on an index / memory bank): consistent with the “empirically evaluable” pitch in the transformation-induced cover line.
    - Zhu, An, Huang (NeurIPS 2021): [https://arxiv.org/abs/2106.12052](https://arxiv.org/abs/2106.12052)
### High-leverage papers to add to your list
#### Metrics/theory for when invariance helps
- Zhu, An, Huang (NeurIPS 2021): [https://arxiv.org/abs/2106.12052](https://arxiv.org/abs/2106.12052)
- Tahmasebi & Jegelka (NeurIPS 2023): [https://arxiv.org/abs/2306.04667](https://arxiv.org/abs/2306.04667)
- Cohen & Welling (ICML 2016): [https://proceedings.mlr.press/v48/cohenc16.html](https://proceedings.mlr.press/v48/cohenc16.html)
#### Representation changes that linearize group actions (closest to your examples)
- Lift-Splat-Shoot (Philion & Fidler, 2020): [https://arxiv.org/abs/2008.05711](https://arxiv.org/abs/2008.05711)
- RAVEN (Klee et al., 2026): [https://openreview.net/forum?id=b90f264ff3216c591bf2ed4ce88eae7b9745f7ab](https://openreview.net/forum?id=b90f264ff3216c591bf2ed4ce88eae7b9745f7ab)
- EquivAct (Yang et al., 2024): [https://arxiv.org/abs/2401.09531](https://arxiv.org/abs/2401.09531)
- Polar Transformer Networks (Esteves et al., 2018): [https://arxiv.org/abs/1709.01889](https://arxiv.org/abs/1709.01889)
#### RL-specific equivariant representation learning
- EqR: Mondal et al. (ICML 2022): https://proceedings.mlr.press/v162/mondal22a/mondal22a.pdf
### Concrete next steps
1. **Define “metric works”** as a _ranking criterion_ across representations ($\phi_k$) that correlates with equivariant-vs-baseline sample efficiency on the same task.
2. **Replace raw ($\mathcal{M}_{haar}$)** with an _advantage statistic_ aligned to occupancy (your $p(g)$), and normalize by a data-resolution scale.
3. **Add a symmetry-compatibility check** from weak-policy rollouts (one-step transition/reward equivariance test in sim).
4. **Run two environments**: one clean (SO(2)/SE(2) toy) and one robotics-realistic (BEV / rays / object-centric).
5. **Bake in ANN search early** (HNSW/Faiss) so your metric is actually “cheap."
## DeepThink Response
**Enforcing equivariance to "hallucinate" new data points in empty space is completely useless if the optimal policy (or validation distribution) never actually visits those regions.** In RL, sample efficiency is strictly governed by the state-visitation distribution $d^{\pi}(s)$. If a mathematical symmetry maps a realistic state into a configuration that the physics engine or task never naturally produces, the network learns a constraint for a zero-measure set, yielding zero practical benefit.

Here is a comprehensive framework that builds on your insights, answers your questions about deep learning theory and algorithmic complexity, and provides concrete next steps for your paper.
### 1. Fixing the Metric: "Cross-Distribution Orbit Coverage"
To mathematically formalize your insight (that orbits must cover the _useful_ states), your metric must not measure the internal expansion of the training set. Instead, it must measure **how much closer the group orbits bring your available training data to the states you actually need to predict.**
Let $\mathcal{D}_{train}$ be the set of states your agent has explored so far (e.g., from a random or weak behavioral policy $\mu_0$). Let $\mathcal{D}_{val}$ be a batch of states sampled from the target "useful life" distribution (e.g., states from an expert policy, or just a holdout validation set).
- **Standard Coverage Distance:** How well does the raw training data cover the validation data?
$$ D_{base} = \frac{1}{|\mathcal{D}_{val}|} \sum_{x \in \mathcal{D}_{val}} \min_{y \in \mathcal{D}_{train}} | x - y | $$    
- **Orbit Coverage Distance:** How well do the _orbits_ of the training data cover the validation data?   $$ D_{orbit} = \frac{1}{|\mathcal{D}_{val}|} \sum_{x \in \mathcal{D}_{val}} \min_{y \in \mathcal{D}_{train}, g \in G} | x - g \cdot y | $$
**The Equivariant Advantage Score ($\gamma$):**
$$ \gamma = \frac{D_{base}}{D_{orbit}} $$
**Why this perfectly solves your critique:**
Because the outer expectation is strictly over $x \in \mathcal{D}_{val}$, hallucinating points into empty space does nothing. If the group $G$ expands $\mathcal{D}_{train}$ into unvisited space, those new points will not be the nearest neighbors to any $x \in \mathcal{D}_{val}$. Therefore, $D_{orbit} \approx D_{base}$, and $\gamma \approx 1$ (zero benefit). However, if $\mathcal{D}_{train}$ is sparse, and the group action $G$ successfully maps your limited training data _exactly onto the manifold of your validation data_, $D_{orbit}$ plummets, resulting in $\gamma \gg 1$.
### 2. Answering Your Question: Deep Learning Theory

> _[Question] "How does this integrate with current theory on how deep learning works so well? Is this a general statistical idea, with deep theorems that still hold in the case of deep learning?"_

Your skepticism regarding standard covering numbers is well-founded. Classical VC-dimension and covering bounds often become vacuous (e.g., predicting an error bound $\ge 100\%$) for massively over-parameterized deep networks.
However, **Geometric Deep Learning is the major exception where the statistical theory holds up beautifully.** While bounding the _absolute_ error of a deep network is hard, bounding the _relative_ improvement of an equivariant network over a standard network is mathematically rigorous.
When you use a $G$-equivariant network, you are forcing the network to learn a function on the **Quotient Space** $\mathcal{S}/G$ (the space of orbits).
- **The Deep DL Theorems:** Recent papers using PAC-Bayesian bounds and Rademacher Complexity have strictly proven that if the target function is $G$-equivariant, the sample complexity of a deep neural network is strictly reduced by a factor of $|G|$ (for finite groups) or proportional to the dimension reduction $\dim(G)$ (for continuous Lie groups)—**regardless of how overparameterized the network is.**
- **Papers to Read & Cite:**
    - **Elesedy & Zaidi (ICML 2021) - _"Provably Strict Generalisation Benefit for Equivariant Models"_:** The gold-standard mathematical proof that equivariance strictly reduces sample complexity in deep networks.
    - **Bietti et al. (NeurIPS 2021) - _"Sample Complexity of Deep Symmetrized Networks"_:** Directly connects covering numbers, deep learning, and group volume.
Your metric $\gamma$ acts as the empirical bridge: it measures how completely a specific representation $\phi$ satisfies the mathematical prerequisites necessary to trigger the sample complexity reductions proven by Elesedy & Zaidi.
### 3. Answering Your Question: Algorithmic Complexity
> _[Question] "Given that 'simple to compute' is in the sales pitch... don't we have to worry about the algorithmic complexity of this measure? How can we reduce this?"_

Yes. The exact nearest-neighbor calculation is $\mathcal{O}(|\mathcal{D}_{val}| \cdot |\mathcal{D}_{train}| \cdot |G|)$, which is far too slow to run over an entire replay buffer.
You can reduce this to practically $\mathcal{O}(1)$ (constant time with respect to the total dataset size) using three tricks:
1. **Mini-batching:** Because your metric is an expectation, sample a random batch of $B=256$ validation states and $B=256$ training states. The law of large numbers guarantees a stable estimate.
2. **Approximate Nearest Neighbors (ANN):** Use `scipy.spatial.cKDTree` or Facebook's `FAISS` library. Building a KD-Tree on the augmented training batch takes $\mathcal{O}(B|G| \log(B|G|))$. Querying the $B$ validation points against the tree takes $\mathcal{O}(B \log(B|G|))$.
3. **Monte Carlo Group Sampling:** If $G$ is a continuous group like $SO(2)$ or $SE(2)$, do not uniformly discretize 64 bins. Randomly sample $K=3$ to $5$ group elements per training state.
With these optimizations, computing $\gamma$ takes single-digit milliseconds on a CPU, allowing you to log it live during validation loops.
### 4. Addressing Symmetry Breaking (Task Compatibility)
> _[Comment] "Measuring symmetry breaking is definitely another thing to compute."_

This is the most critical hurdle for RL. A representation $\phi$ might expose a beautiful geometric symmetry (yielding a huge $\gamma$), but if the environment's transition dynamics $P$ or reward $r$ break that symmetry (e.g., gravity makes "up" fundamentally different from "down"), equivariance will actively hurt the agent.

You must combine your geometric advantage with a **Task-Symmetry Penalty ($\mathcal{E}_{MDP}$)**. Using a batch of transitions $(s, a, r, s')$ from your buffer:

$$ \mathcal{E}_{MDP} = \mathbb{E}_{s, a \sim \mathcal{D}, g \sim G} \left[ \big| r(s,a) - r(g \cdot s, g \cdot a) \big| \right] $$

_(If you have access to a world model, you can add a similar penalty for $P(\cdot | s, a)$ vs $P(\cdot | g \cdot s, g \cdot a)$)._

The ultimate "Equivariance Suitability Predictor" for a representation $\phi$ becomes a combined function of high Data-Orbit Alignment ($\gamma$) and low Task-Symmetry Violation ($\mathcal{E}_{MDP}$).
### 5. Actionable Experimental Roadmap for Your Paper
To structure this into a high-impact paper (e.g., NeurIPS, ICLR, CoRL), here is a logical progression:
**Experiment 1: The Zero-Shot Predictor (The Reacher/Nav Task)**
- Set up your 2D point-goal navigation or Reacher-V5 task.
- Define 3-5 different parameterized representations $\phi$ (e.g., Raw Cartesian pixels, Polar Object-centric coordinates, and representations with varying degrees of nuisance noise/crops).
- _Before_ RL training, compute your metric $\gamma$ and $\mathcal{E}_{MDP}$ for each representation using a random play buffer.
- Train Equivariant SAC/PPO agents on each representation.
- **The Money Plot:** Create a scatter plot with your predicted metric on the X-axis and the actual Empirical RL Sample Efficiency (e.g., Area Under the Reward Curve) on the Y-axis. A strong positive correlation empirically proves your metric works.

**Experiment 2: The "Nuance" Experiment (Proving the Empty Space Insight)**
To explicitly prove _why_ your cross-distribution metric ($\gamma$) is better than standard data-augmentation metrics:
- Design an environment with an obstacle that restricts the agent to only a 90-degree quadrant of the board.
- A naive density metric ($\mathcal{M}_{haar}$) will give a huge score to $SO(2)$ equivariance because it hallucinates data in the other 270 degrees. But your corrected metric ($\gamma$) will realize the validation set _also_ never visits those 270 degrees, correctly yielding $\gamma \approx 1$. Show that the RL agent actually gains little sample efficiency here.
**Experiment 3: Auto-Tuning the Representation**
- You asked Cyrus: _"Can we use this measure in order to learn a representation?"_ **Yes.**
- If you implement your nearest-neighbor distance using a differentiable Soft-Min operation (e.g., a Gaussian Kernel Density Estimator or LogSumExp), your evaluation metric becomes a **differentiable loss function**.
- You can train a neural network encoder $\phi_\theta$ to _learn_ a representation that maximizes $\gamma$ directly from offline data, without ever running RL. Then, apply Equivariant RL on top of this natively learned representation.
Your intuition is significantly sharper than the standard AI boilerplate. You have identified a highly novel intersection: using fast, cross-distribution manifold geometry to predict representation quality for equivariant RL. Keep pulling at this thread!
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

# February 19, 2026
## Experiment
The goal of this experiment is to do some testing of equivariance gain predictors on toy models.
Toy model:
- Reacher. Code up 3 different equivariant representations.
	- $r = x_{\text{Goal}} -  x_{EE}$.
	- $r_{1} = x_{Goal}, r_{2} = x_{EE}$.