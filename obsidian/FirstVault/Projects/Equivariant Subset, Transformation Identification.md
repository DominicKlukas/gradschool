## Idea
You have an observation $\mathcal{O}$. In the given observation, you don't have meaningful equivariance. However, if you transform the space, you can define a set of transformations on that space which work nicely.
### Setup

Let $(\mathcal{S}, \mathcal{A}, P, r)$ be a Markov Decision Process (MDP), and let
$$
\pi^* : \mathcal{S} \to \mathcal{A}
$$
be an optimal deterministic policy.

Define the *state--action graph of the optimal policy* as
$$
\mathcal{X} \coloneqq \{(s, \pi^*(s)) \mid s \in \mathcal{S}\}.
$$

Let $\mu$ denote the *occupancy measure* induced by $\pi^*$:
$$
\mu(s,a) \;=\; \lim_{T \to \infty} \frac{1}{T} \sum_{t=0}^{T-1}
\mathbb{P}_{\pi^*}(s_t = s, a_t = a).
$$
The support of $\mu$ lies in $\mathcal{X}$.

### Equivariance on State--Action Spaces}

Let $G$ be a group.

### Equivariance of the Optimal Policy

We say that $\pi^*$ is **$G$-equivariant on $\mathcal{S}$** if there exist representations
$$
\rho_{\mathcal{S}} : G \to \mathrm{Aut}(\mathcal{S}), 
\qquad
\rho_{\mathcal{A}} : G \to \mathrm{Aut}(\mathcal{A})
$$
such that
$$
\pi^*(\rho_{\mathcal{S}}(g)s)
\;=\;
\rho_{\mathcal{A}}(g)\,\pi^*(s)
\quad
\forall g \in G,\; s \in \mathcal{S}.
$$

Define the induced action on the state--action space:
$$
\rho_{\mathcal{X}}(g)(s,a)
\;=\;
(\rho_{\mathcal{S}}(g)s,\; \rho_{\mathcal{A}}(g)a).
$$

The policy $\pi^*$ is equivariant if and only if $\mathcal{X}$ is invariant under $\rho_{\mathcal{X}}$.

### Equivariance and Sample Efficiency

For $(s,a) \in \mathcal{X}$, define its *orbit*:
$$
\mathrm{Orb}_G(s,a)
\;=\;
\{\rho_{\mathcal{X}}(g)(s,a) \mid g \in G\}.
$$

Equivariance yields a meaningful inductive bias when
$$
\mu(\mathrm{Orb}_G(s,a)) \;\gg\; \mu(\{(s,a)\}),
$$
so that a single observed pair represents many equally likely ones.

### Observation Spaces and Policy Equivalence

Let $\mathcal{O}$ be an observation space, and let
$$
\phi : \mathcal{S} \to \mathcal{O}
$$
be an information preserving (not necessarily injective) observation map.

#### Policy-Equivalent Spaces

We say $\mathcal{S}$ and $\mathcal{O}$ are *policy-equivalent* if
$$
\pi^*_{\mathcal{O}}(\phi(s)) = \pi^*(s)
\quad \forall s \in \mathcal{S}.
$$
In that case, we can define the induced optimal policy on observations:
$$
\pi^*_{\mathcal{O}}(o)
\;\coloneqq\;
\pi^*(\phi^{-1}(o)),
$$
assuming $\phi$ is invertible on the support of $\mu$.
### Equivariance via Representation Change

#### Main Phenomenon

It may occur that:
1. No nontrivial group action $G$ makes $\pi^*$ equivariant on $\mathcal{S}$, or any group action $G$ does not result in greater sample efficiency.
2. There exists a representation
$$
\rho_{\mathcal{O}} : G \to \mathrm{Aut}(\mathcal{O})
$$
	and a representation
$$
\rho_{\mathcal{A}} : G \to \mathrm{Aut}(\mathcal{A})
$$
	such that
$$
\pi^*_{\mathcal{O}}(\rho_{\mathcal{O}}(g)o)
\;=\;
\rho_{\mathcal{A}}(g)\,\pi^*_{\mathcal{O}}(o)
\quad \forall g \in G,\; o \in \mathcal{O}.
$$
	and the equivariance is useful, so that $\mu(\text{Orb}_{G}(s, a)) \gg \mu(\{s, a\})$.
In this case, equivariance is *realizable only after representation change*

### Equivariance-Inducing Representations

We say $\phi$ is *equivariance-inducing* if there exists a representation
$\rho_{\mathcal{O}}$ such that
$$
\phi(\rho_{\mathcal{S}}(g)s) = \rho_{\mathcal{O}}(g)\phi(s),
$$
even when $\rho_{\mathcal{S}}$ is trivial.
- The original state space may lack exploitable symmetry.
- A transformed observation space can reveal latent geometric structure.
- Equivariance becomes meaningful only in the lifted representation.

### Summary

Even when an optimal policy admits no useful equivariance on the true state space,
there may exist a policy-equivalent observation space supporting a nontrivial group
action under which the optimal policy becomes equivariant, yielding meaningful
inductive bias and improved sample efficiency.


## Papers to Read
- Lift Splat Shoot
- RAVEN: End-toend Equivariant Robot Learning with RGB Cameras
- EquivAct: SIM(3)-Equivariant Visuomotor Policies beyond Rigid Object Manipulation


# Experiments

## Experiment 1: Dot position on circle
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


# Experiment 2: 