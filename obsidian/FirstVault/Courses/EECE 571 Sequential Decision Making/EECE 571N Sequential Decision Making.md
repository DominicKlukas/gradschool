The textbook is [[Markov Decision Processes, Puterman]], chapters 4 through 10.
So far, we looked at the definition of RL problem (state space - gives us all the information we need to make the best decision at this point/action space/transition function), the gridwold problem (we learned how important it is to define what our reward functions are) that actions can be a function of state space.

Next example: Autonomous Taxi Example. **Example of how to model as RL problem**.
Again, we consider the state space/action space/transition function, for this simple world where the taxi has different locations it can drive to.
- Consider the location of the taxi, the location of the customers that are waiting, the destination of the passengers, and which passengers are in the car/what their destinations are.
- Action space: pickup/dropoff passenger. Move between adjacent locations.
- Transition function: $T(s' | s, a)$ (defines a probability). $s \in S$. Pickup: then passenger is in car. Passenger in the car: go to location: get reward, passenger leaves, etc.

A **decision rule**, $d_t$ is a function specifying an action to be executed at an individual decision epoch $t$.  
Decision rules can have different properties:
- It is *history-dependent* if it relies on previous states and actions: $d_t(s_0, a_0, ..., s_t)$ and then gives us an action to take at the current time. It is *Markovian* if it only relies on the current state, $d_t(s_t)$. (state doesn't give you enough info)
- Also, can be *deterministic* or *random* if it outputs a single action, versus a distribution.
We can have any mix of these, denoted HD, MD, HR, MR.

A policy is a sequence of decision rules. Belongs to a policy class if in same class (HD, MD, HR, MR), respectively. A policy is stationary if the decision rule is constant in time.

Common objective function:
$$ \pi^* \in \arg \max_{\pi \in \Pi^{HR}} \mathbb{E}\left[ \sum_{t=0}^{\infty} \gamma^t r_t | \pi, s_0 \sim \mu \right] $$
Fixing a policy in an MDP fixes a Markov chain (matrix with states as bases, and columns sum to 1).

When we fix a policy, we have a set of possible trajectories (which have a given probability given the sigma algebra/probability space we are dealing with). Every trajectory (sequence of states/actions) has a given reward/discounted reward, and that is what we are taking the expectation over (different trajectories).

From this perspective, we can also consider the expected value from a given state (by computing its discounted reward). That is $V^{\pi}(s) = \lim_{N \to \infty} \mathbb{E} \left[ \sum_{t=0}^N \gamma^t r_t | \pi, s_0 = s \right]$. What assumptions did we make?
- We assume that this infinite sum converges. However, it does, by the geometric series, when $r$ is bounded. This tells us why the discount factor is important.
- It doesn't depend on the current time (which is a Markov property) about the whole problem. This only works for stationary policies and infinite time horizons.
$Q^{\pi} (s, a) = \mathbb{E} \left[ \sum_{t=0}^{\infty} \gamma^t r_t | \pi, s_0 = s, a_0 = a \right]$ is a similar concept. You can quickly and easily compute between the two of them. Typically you will see the $Q$ value because it is very convenient to be able to search actions.

Optimal policy defined in the obvious way, for policies in HR, since this is the "biggest" policy space. Optimal policy may not exist in a smaller policy space. Thm 5.5.3 in Putermen. (It's an interesting proof, so read it!)

## Summary of Lecture 2
- We introduce the MDP, which is $\mathscr{M}(S, A, T, R, \gamma, \mu)$. (First 13 slides).
- We introduce decision rules, which determine which action to take at time t. 4 options: HD, MD, HR, and MR, and stationary.
- We define the optimal policy, and explore the mathematical objects underlying the expectation function. Based on this definition, we also define metrics V and Q.
- We claim that the optimal policy exists in MD space.

# Bellman's Equations & Dynamic Programming

The value function depends on the policy. $V^{\pi} (s)$... it is a function of $\pi$. For today's lecture, we will be going through Chapter's 6.1-6.4 of Puterman's book.

Tower property: $\mathbb{E}[x | z] = \mathbb{E} [\mathbb{E}[x|y,z]|z]$ average of something given info on z, is equal to first averaging over more detailed info $y$ and $z$ and then averaging the results of that average over $z$.

Belleman's equation is computed as the expectation of the value of a state given a certain policy. This is the foundation of dynamic programming.

## Summary of Lecture 3
- We define a policy to be optimal if it maximizes expected reward, and compute quantities of interest $V$ and $Q$ respectively. From the definitions of $V$ and $Q$, we derive (using the rigorous definition it is clearer):
$$V^\pi(s)= \sum_{a \in A} \pi(a|s) \left(R(a,s) + \gamma\sum_{s' \in S} T(s'|s, a) V^\pi(s) \right) $$
- We solve using dynamic programming, in 3 steps: we fix a policy, and use DP to solve for $V^\pi (s)$. Then, we "look" and see how the policy is being inconsistent and making bad decisions, w.r.t the values it gets in states based on its current decisions. We update the policy to make the best decisions w.r.t. it's own values and iterate.
- 
# Value Iteration
We derive the following equation:
$$ V^* (s) = \max_{a \in A} \left[ R(s, a) + \gamma \sum_{s' \in S} T(s' | s, a) V^* (s') \right] $$
Define the following operator, which will iterate on $V$:
$$ (T_* V)(s) = \max_{a \in A} \left[ R(s, a) + \gamma \sum_{s' \in S} T(s' | s, a) V^* (s') \right]$$
How do we show that this converges?
- First step: show that Bellman optimality operator is a contraction mapping.
- Then, by Banach fixed point theorem, $T^*$ must have a unique fixed point.
- Since $V^*$ is a fixed point of $T_*$ by definition, the iterative procedure must converge to the unique fixed point $V^*$.
- Optimal policy $\implies$ we can do policy evaluation to find the optimal value function.
- Optimal value function $\implies$ we can extract the optimal policy by solving a one-step maximization problem.
Once we have this optimal value function, we can quickly get the optimal policy!
Often the assumptions required to make these things work don't hold... and modifications/reconsideration must be taken.
- Rewards might not always be scalar!
- Our environments might be partially observable as well!
- Reward/dynamics that depend on time.

Going forward: we estimate the optimal values/optimal policies.

## Solving MDPs with LP
The constraints enforce that the solution is bigger than all the alternatives.

The linear programming introduces two new variables: the initial state probability, alpha, and the "occupancy rates" $x_{s, a}$. $x_{s, a}$ denotes the "occupancy rate", which is related to the distribution of the policy by
$$ \pi(a | s) = \frac{x_{s, a}}{\sum_{a' \in A} x_{s, a'}} $$
It kind of signifies how often you will be taking an action. If you look at the expression (on the slides) which defines this expression, then you will see that the discounts are built into it.

We can also solve finite horizon problems with LP, by having variables for each action in time (and for the dual problem, for every occupancy rate).

The HJB PDE in the continuous case can be formidable.
A "nasty" PDE can have something called "kinks"... what is the intuition? Chaos theory! Starting at state x might end in one solution, and x+epsilon might end up in one in a completely different domain! (Like if we are on either side of a knife edge).
But there interesting thing, is that once you add stochasticity into your problem, you can get much smoother solutions, because they smooth out this kink into a nicer gaussian.


# Partially Observable MDPs
Up until now, we have assumed that we have known the transition function and the state perfectly at any given point in time. Now, we will weaken this assumption, and assume that we know the transition function perfectly, but we do not know the state of the system perfectly.

We add two more objects to our MDP: $\Omega, O$. Thus: $\mathscr{M}(S, A, T, R, \gamma, \mu, \Omega, O)$.
- $\Omega$ is the Observation set. $O$ is the observation functions. The Function $O(o | s', a)$ maps states and actions to distributions over observations $o \in \Omega$. 
- We have that $O$ is a function of the action, because sometimes the action that you take will determine which observations you can take (for example if you want to take an action that lets you drop a sensor).
- In general, relies on histories of observations and actions $\pi(a | h_t)$, where $h_t = o_0, a_0, o_1, a_1, ..., o_t$. To store every possible sequence of observations, and an appropriate response for each of them will require exponential memory in time.
- Belief states are probability distributions over the states. We update them every step with a cool expression derived in the slides.

The expression is $b_{t+1}(s') = \nu O(o_{t+1} | s', a_t) \sum_{s \in S} T(s' | a, s) b(s)$. Before we make our observation, we can easily derive our guess $\bar b_{t+1}(s') = \sum_{s \in S} T(s'|a, s)b(s)$. Now, how do we go from this to our updated belief distribution?

We would have:
$$ b_{t+1}(s')= P(B) = \frac{P(B | A) P(A)}{P(A | B)} =  \frac{Pr(o_{t+1} | s', a_t) \cdot Pr(s' | h_t, a_t)}{Pr(o_{t+1} | h_t, a_t)} $$
But then, we can see that the denominator is a normalizer, the left factor on the top is the $O$ factor and the factor on the right is just our prior guess.
- But now, if we wanted to solve this with DP, then we would have infinitely many final states.
- Instead, we can break the simplex up into a discrete number of points. However, state space is huge and continuous. For $|s|=n$, belief space is continuous and of dimension $n-1$. Solving discrete MDP is intractable. Grid discretizing the belief space, suffers from curse of dimensionality: if we have 19 states, then we need to discretize each dimension into 20 bins, the resulting discrete belief space has $\binom{k + n + 1}{n - 1} \approx 3.36 \times 10^{10}$ states. This is called the (stars and bars combinatorial problem).
- Backups require summations over every possible observation, so large observation spaces (e.g. Images) mean we have intractable Bayesian filtering.
- **This is an incredibly hard problem!!** (Moral of the whole lecture).
- We can use Deep Learning to learn actions from states.
# Exploration and Bandit Problems
Assumptions that we have been making so far:
 - We know a model of the system: i.e. we have access to exact functions $T(s', s, a)$ and $R(s, a)$.
	 - If we remove these assumptions, we now need to approximate $V^*(s)$ and $\pi^*(a, s)$ from data. This is what RL is.
	 - Two important ones: 
		 - Model-based RL: first learn an approximation for the things that we are missing: $\tilde{T}(s'| s, a)$ and $\tilde{R}(s, a)$ and then, use them to estimate $V^*(s)$ or $\pi^*(a|s)$ directly. This was a hiccup for some students. They were wondering: what does it mean for the reward to be unknown? The fact of life is that it means that we can't be sure what reward we will get (or the distribution of the rewards) will be.
		 - Model-free RL: Learn $V^*(s)$ and or $\pi^*(a|s)$ directly from data. People like this because of
We introduced the concepts of exploration and exploitation.
In general, when is RL useful?
- Unknown parts of the MDP means we can't solve directly.
- When we don't even know how to transform inputs/perception into representations of information that's relevant to our decision making.
- Even with perfect simulation, RL can be useful to extract/learn a policy.
- Algorithms are very general. Can "learn" good behaviors from simulations in cases where it is not so easy to analytically write down what the dynamics are.
- With POMPDs, even a finite state MDPs, writing up Belleman backups can be intractable. But sampling the value at a state is tractable.

## Bandit Problems
- Ad selection, Medical trials, Investment: each action (selecting an ad, medicine, stock to invest) has a stochastic reward (probability of making a certain amount of money), and you are trying to find out what the maximum possible reward will be.
- One state MDP with an unknown, stochastic reward function. Every action brings us back to the previous state, but we get a different reward for any action.
For now, let's assume we are trying to find the mean reward of each action, and exploit the action with the highest mean reward.
At round $T$, how much does the agent regret not knowing the best action in advance? What is the most money we possibly could have made (on average, by making the decisions we made)?

### Uniform exploration algorithm
Explore each of the $k$ bandits $N$ times. Compute the average for each. Then, exploit the best and play it all the remaining rounds. What will our regret be?

First, we use a bound for the inequality: $P(|\mu - \hat\mu| \geq \epsilon)$ in order to find out the number of times we would have to try an action in order to see what probability this is. (We want this probability to be low). The math is nice, if we want a probability to be $\delta = \frac{2}{T^4}$. Then, we get:
$$
P\left(|\mu - \hat\mu| \leq \sqrt\frac{2 \ln (t)}{n_t(a)}\right) \leq 1 - \delta
$$
We are seeking to compute the expected regret.
We compute the expected value, by breaking possible events into "clean" and "failure" events, in the cases where our estimations are or are not within the calculated bounds.
We can then use the radius, to show that if we pick the wrong action, then the true mean for the wrong pick and the right pick satisfy
$$ \mu(a) + \text{rad}_T \geq \hat\mu(a) > \hat\mu(a^*) \geq \mu(a^*) - \text{rad}_T $$
Thus, $\mu(a^*) - \mu(a) \leq 2 \text{rad}_T$, so that $R(T) \leq N + 2 \text{rad}_T(T - 2N)$. Now, to minimize regret, choose $N$ appropriately to minimize this.
In the case where we don't have a clean event, we have $T$ as an upper bound for the regret conditioned on failure event (wrong every time) but then, since the expectation of failure is $O(T^{-4})$, we are OK with this because it goes to zero quickly.
These theoretical bounds are useful! We can do similar ones for the $k$-armed bandit.

### Epsilon-Greedy Algorithm
- With probability $\epsilon_t$ choose an action uniformly at random
- With probability $1- \epsilon_t$, take the action with the highest expected average reward.
- At each time, update your expected average reward.
### Successive Elimination
There are also adaptive version: they eliminate options if they have confidence intervals where the upper confidence interval is lower than the lower confidence interval of any other interval. This is called "successive elimination".

### Optimism under uncertainty
(UCB1)
- Try each action at least once. After that, compute: $UCB_t(a) = \hat\mu_t(a) + \sqrt{\frac{2 \log(t)}{n(a)}}$.
- Choose the action which maximizes this.
- Naturally has a really nice balance between exploration and exploitation.

### Thompson Sampling
- We have a posterior distribution which you generate with the samples you have collected so far. We choose it to be a beta distribution, because many shapes can be updated with just 2 parameters.
- Each time, you sample from all of the distributions you have parameterized so far: you choose the one which you simulated to be the best.

We can use UCB1 on tree searches, or also incorporate previous exploration knowledge.

## Monte Carlo Methods
We explored exploration and exploitation, in the context of bandits, already. We didn't really consider value functions.

First, we consider episodes. In the real world, we don't sample infinite time series: it is always a finite time horizon. The agent always finds himself in some self absorbing state.

Why do we want to learn from our environment?
1. We don't know anything about the environment.
2. We have a perfect simulator, but it's hard to solve the problem via dynamic programming.

What do we want to estimate from our sampled episodes?
- Policies
- Reward functions
- State-action value functions
- Transition probabilities
Once we have these... what do we do with them?

Model-Based RL: Learn the reward functions, and transition 
Model-Free RL: Approximate the appropriate state-action value functions from data?

RL is about learning DP quantities from data.

Gymnasium: you build a wrapper around your simulator which interfaces with your environment through gymnasium. Just requires a couple methods in your class, in particular step and reset. This makes using different algorithms very convenient, because so long as you respect the interface, you can do pretty much anything!

Now, to Monte Carlo Methods!

### Generalized Policy Iteration
- Start with some policy $\pi$
- Compute $V^{\pi}(s)$
- Make $\pi'$ greedy w.r.t. $V^{\pi}(s)$
- Repeat until $\pi \to \pi^*$
This is not a standard term, but rather a way of thinking about them. Don't need convergence, and refinement can be courser (you estimate $V$, don't go so far).

Monte-Carlo Method, in general, is sampling a random variable in order to determine it's properties.

Given $\pi$, we want $V^{\pi}(s) = \mathbb{E}[G_t, S_t = s]$ where $G_t = R_{t+1} + \gamma R_{t+2} + ...$ . 
(We assume )
We estimate this, from an initial state $s_I$ by rolling out a bunch of trajectories and taking the average of this reward.
How can we estimate infinite sums from finite episodes?
Episode is a trajectory that ends in a terminal state or after a fixed horizon.
If a terminal state is reached, then the rewards are zero thereafter. As long as every trajectory ends in a terminal state, it doesn't matter.
If we are dealing with cases where there are no terminal states, having a finite episode means we truncated the episode.
- Estimating $G_t$ with small $t$ and $\gamma < 1$ means later contributions at the end don't matter.
- On the other hand, $G_t$ with $t$ close to $\tau$ artificially truncates future rewards.

then, we sample episodes, compute the reward for each, and estimate the value as the mean of these.

- First-visit MC: in each episode, if we hit state $s$ multiple times, we only count the return from the first time we see it.
- Every-visit MC: Count the return after every time we see $s$ in an episode. This is a way to get more data! Nice.

Blackjack sim is easy.
Writing out a transition function that is correct is hard.
That's why it is useful to only need samples from sim and not an explicit transition function for your policy, so model free is useful.

Philosophically speaking, DP relies on estimates for every single state to help calculate estimates for neighboring states. But MC deals with every single state. But the recursive nature that DP uses is helpful at the end of the day. MC need tons and tons of states in order to help you out.

DP spreads information everywhere with each sweep but it needs a model.
MC spread information only where we've been, but it doesn't need a model.


## Reinforcement Learning
- Our problem was that often we don't have the reward or transition functions, so we can't simply compute $V$ and then have our policy already.
- Instead, we can learn $Q^{\pi}(s, a)$. Then, we can just compute: $$
\pi(a, s) = \text{argmin}(Q^{\pi}(s, a))
$$
- We can update these with Monte Carlo tree search in the same way we were updating $V$ with Monte Carlo methods before.
- Problem: we often won't visit every single state action pair... but you can use different techniques in order to do it. Exploring starts: you have an initial distribution even over the entire set of state action pairs, and then roll out trajectories from there.
- Again, we can alternate between improvement and exploration, (instead of doing thousands of Monte Carlo runs on a bad policy just to get an accurate estimate of how accurate it is), update your policy before you have a perfect guess for the Q values. This should in theory converge.
- You can also do **$\epsilon$-soft policies**. Basically, you choose your optimal action most of the time, and then with probability $\epsilon$ choose some other policy.
	- We proved in class that we get policy improvement. Potentially read the textbook.
	- It doesn't learn the optimal policy.
- ON Policy: we are exploring on the data we are learning. The policy we are learning the behavior about is the one we are learning. All of the methods we learned so far were ON policy.
### Off Policy Learning
OFF Policy: we use data from the policies we have done before, or other data, in order to learn what we would do better in the policy that we have.
- The technique is called Importance sampling.
- We can compute something called the likelihood ratio: it is the likelihood of a specific trajectory if we use one policy vs another policy, and use this then to compute values for my $V$ or $Q$ values.
- This is a very important concept in RL, so that you can use other data, offline data, data from a dataset, in order to update your own policy.

# Temporal Difference Learning
Combines DP and Monte Carlo methods into one. Very powerful way of doing things!
The running average formula is typically $\mu_{n} = \mu_{n-1} + \frac{1}{n}(x^{(n)}-\mu_{n-1})$. In RL, we often replace $\frac{1}{n}$ with a constant step-size parameter $\alpha \in (0, 1]$.
That is: $$
\hat{\mu}_{n} = \hat{\mu}_{n-1} + \alpha (x^{(n)} - \hat{\mu}_{n-1})
$$
This reduces how much we are updating the new average based on our new sample, resulting in a more stable learning formula. If we expand this out:
$$
\hat{\mu}_{n+1} = (1-\alpha)^{n} \hat{ \mu}_{0} +  \sum_{i=1}^{N} \alpha (1 - \alpha)^{i}x^{(i)}
$$For TD learning, we compute:
$$
\hat{V}(s_{t}) = \hat{V}^{\pi}(s_{t}) + \alpha (r_{t} + \gamma (r_{t} + \gamma \hat{V}^{\pi} (s_{t + 1}) - \hat{V}^{\pi}(s_{t}) ))
$$
Essentially, we compute the average of $R_{t} + \gamma\hat{V}$ instead of just $\hat{V}$.


### SARSA
We use temporal difference learning to get value estimates for $Q(s, a)$, and then use policy iteration to follow an $\epsilon$-greedy exploration policy.

We will look at some tabular explore/exploit algorithms which learn the transition and reward functions.
### Explicit Explore Exploit ($E^3$) algorithm
- Maintain an empirical model of the environment $\hat{T}(\cdot | s, a), \hat{R}(s, a)$ and a notion of what portions of the MDP are known vs. Unknown. If the model is confident, exploit it, if not explore it.
- It explicitly separates out exploration and exploitation.
	- If I've seen this state action transition enough times, then my prediction of the distribution where I'll end up next, is accurate to some degree. (Concentration inequalities).
	- Note: prior bounds and convergence was all asymptotic.
	- There is a theorem: if your reward and your state transition functions are close enough (defined in terms of epsilons and deltas) then you can say that your value will be sufficiently accurate as well!
	- Use concentration inequalities to derive the number of samples required so that the assumption of closeness to reward function and transition function hold.
- Next, we define an induced MDP $M_{s}$ which creates an abosrbing state connected to all of the unknown states so that we can either create a near-optimal policy for the true MDP, or create a policy that quickly reaches the abosrbing state to continue exploration.

The algorithm:
- In each unknown state, select the action that has been selected the fewest times in the past
- Once you have visited a state "enough" times add it to the set of known states $\mathcal{S}$.
- When a known state is reached
	- construct the induced MDP over the current set of known states
	- Try to exploit, compute optimal policy in $M_{s}$ and see if it is $\epsilon$-close to $V^{*}_{M}$.
	- If you can't compute such a policy, synthesize a policy in $M_{s}$ that reaches the absorbing state as quickly as possible.
	- Return to balanced exploration.

### R-max: Optimistic planning under model uncertainty
Core idea: R-MAX replaces $E^{3}$'s explicit exploration with an optimistic model (unknown state-action pairs give reward $R_{\text{max}}$ and transition to absorbing state), so optimal planning in the model automatically drives exploration.
This is a form of the optimism in the face of uncertainty idea that we saw in Bandits.
But this algorithm was originally developed for stochastic games. But for the sake of the class we can view it in the context of MDP algorithm that simplifies $E^{3}$'s explicit explore or exploit trade-off.

Descendants
- PAC-MDP 
- MBPO, TD-MPC, and TD-MPC 2
- Dreamer papers! (Make sure to read one, perhaps the Minecraft paper).


## Function Approximation in RL
- Instead of having a table for $V$ and $\pi$ functions, we have a parameterized function $V_{\theta}$ and $\pi_{\theta}$ for some parameter vectors $\theta \in \mathbb{R}^{d}$.
- We can have a linear model, or a higher dimensional Neural Network.
Why is it useful?
- You need function approximation in order to use the algorithms we have been discussing so far. As $\lvert \mathcal{S} \rvert$ grows we can't afford to keep track of every $V(s)$ individually. Instead, we want to learn $V_{\theta} (S)$ where $\theta$ is some vector and $d \ll |S|$. We want to generalize. This is only possible because we are expecting our parameterized function $V_{\theta}(S)$ to generalize between states.
- They are good at dealing with partial observabilitiy. They can abstract away unknown data.

The reason why we are trying to minimize $R(f) = \mathbb{E}_{(x, y) \sim \mathcal{D}}[\mathscr{L} (f(x), y)]$ is because, we want our function to approximate better on points that we can be sure will show up more often. This is not a tractable problem, so we instead optimize w.r.t. empirical data. Supervised learning is when we have the data labels $y$ at our disposal.


### Stochastic Gradient Descent
One thing we might want to do is to learn a value function $V_{\theta}(s)$.
To do so, we will want to compute the gradient with respect to $\theta$ of $\mathbb{E}[(V_{\pi} - V_{\theta})^2]$. Stochastic gradient descent samples a random state, and then computes gradient of $(V_{\pi} - V_{\theta})^2$ instead. We can approximate $V_{\pi}$ with a Monte-Carlo estimate, or with a TD estimate (which is a bit circular, because it requires $V_{\theta}$ to compute $V_{\theta}$...). But we make it slighlty more stable by not computing the gradient of $V_{\theta}$ inside of the TD approximation, and this is called the smi-gradient. It learns really quickly and is unsable but slightly more stable than if we had done the true gradient of this difference.

Sutton and Barto says that this does converge to the closest function in your function space that can be expressed by the functions that you have.

Deadly Triad: don't do function approximation, bootstrapping, and off-policy learning all at the same time!

How do modern Deep RL algorithms deal with these issues? They have function approximation, bootstrapping, and off-policy learning.
- Use feature extractors with good inductive biases to avoid correlations between $V(s)$ for different $s$ which shouldn't actually exist.
- RL has a non-stationary learning objective. This problem was made worse by bootstrapping.
	- Freeze a "target network" $V^{\bar\theta}(s)$ or $Q^{\bar\theta}(s, a)$ that is used to define learning updates, and only occasionally update it itself.
- Experience replay/replay buffers: learn from saved batches of data, isntead of from streaming experiences as they come in.

### Deep Q Learning
We input the past 4 image observations, since our system isn't actually Markovian: if you are playing pong, you need more images in order to see the velocity for example.
How to deal with the deadly triad
- The target network helps stabilize the learning problem
- Off policy data is randomly selected, smoothing stuff
- One action in one part of the state space tend to move other predictions in a consistent direction, rather than chaotically. This helps with function approximation.

## Policy Optimization
First, we assumed that if we have a Q function, we immediately have an optimal policy because we can just take the action that maximize this goodness.
Here instead, we parameterize the policy, and we define some metric of the reward that that specific policy gets in the environment, and differentiate that instead.

#### Common Policy Parameterizations

Discrete action spaces
- Softmax distribution: $\pi(a | s) = \frac{\exp(f_{\theta}(s, a))}{\sum_{a' \in A} \exp(f_{\theta}(s, a'))}$.
- How can we implement this? We randomly sample. We implement a neural network that maps state $s$ to a vector of logits $z_{\theta}(s)\in \mathbb{R}^{|A|}$. Then take the softmax and randomly sample an action.
Continuous actions
- $A$ is a subset of $\mathbb{R}^{m}$
- We parameterize deterministic mappings from $S \to A$, or means and covariance matrices of Gaussians as a function of the state which when then sample at runtime.
LLMs "look like" policy gradient methods since they don't spit out value functions on the set of "good" words but rather a policy that spits out actions.

Why are they advantageous over value methods?
- Value methods use bootstrapping, which can cause problems. Pure policy gradient methods don't necessarily have this issue.
- Don't solve a harder problem as an intermediate step. Policy gradient methods don't seek to compute the future values.
- Directly handles continuous/high-dimensional actions spaces
	- We don't have to explicitly solve $\text{argmax}_{a} Q(s,a)$ for every decision. If $Q$ has a continuous output, then optimizing can be a difficult problem.
- Naturally supports expressive stochastic policies.
- Let's us impose structure on the policy itself.
	- We can impose priors on actions better than priors on values.

## Policy Gradient Algorithms
Last class, we showed that the expectation of the improvement of the policy over the entire trajectory, was proportional to the expectation of a function that was actually possible for us to compute: $$
\mathbb{E}\left[ \sum_{t}G_{t} \nabla \ln(\pi_{\theta})(A_{t} | S_{t}) \right]
$$
We can further argue that adding a value to $G_{t}$ as a function of the starting state won't make a difference to the evaluation of the improvement of the policy. (Think about the advantage function: it is the value of taking an action at an initial state minus the value function, which is not a function of the state). But in order to do that, we need both the value function and the policy function.

Just using a biasing on the Monte Carlo estimate is not an actor critic method, even if it is dependent on a learned value function. Bootstrapping, however, is, because the expected value that the function is being evaluated on is a direct function of the critic! It has even less variance, but it does introduce bias.

## Different Algorithms
### PPO
- Still the algorithm still go to.