# AGC, Temporal Logics/ Model Checking Representations
- O2a
	- Develop a common representation for assume guarantee contracts, LTL logic, reward machines, that must capture heterogeneous capabilities, evolving learned behaviors, and asynchronous interactions (to deal with state space problem).
	- Use foundation models to automate contract generation and task decomposition steps.

# Assume Gaurantee Contracts
Assume-Guarantee contracts are built around the abstract idea of a component, of a system. The main operations on components are compositionality, and conjunction. A component satisfies a "contract", if it is a member of the contract. A contract specifies a set of behaviors the environment is allowed to exhibit, and a set of behaviors the component promises to exhibit, if the environment behaves.

Key ideas
- Different "views" can be combined through conjunction... this allows for the integration of multiple design requirements from different compartments.
- Composing systems becomes easy to reason about.
- This framework formalizes the writing of requirements themselves, and the restriction of the available components which results. It organizes them together in a neat systems design framework which rules out bad design choices resulting from integration errors by seeking to unify requirements through reasoning about sets of components which satisfy all of them.

# LTL Logic
LTL logic is one way of describing sets of behaviors through trajectories, such that said behaviors can be feasibly checked through automata so long as a (finite non-terminating) transition system is supplied.

We have focused so much on specifying LTL constraints based on commands... but many of the required constraints for achieving objectives are implied, or intuitive, and difficult to specify exhaustively. Through imitating human behavior, perhaps this intuition is captured by AI systems. That being said, coding models are often given under specified model descriptions, and have to infer what is necessary to complete the task. Furthermore, which specifications are relevant is often heavily dependent on case by case specialization. Perhaps reasoning models are necessary to determine precisely what constraints are necessary. The key contribution that AGCs have to contribute are the idea of separating environmental assumptions and component guarantees, for better fault tracing and compatible design.

How do we know a specification is complete, given what an LLM fills in "intuitively" verses what needs to be specified for it to complete the task?
Reward machines in some way also fit into this abstraction: it breaks the task down into actions that need to be clarified for the MA system to work, and then the RL algorithm learns the rest.
Lets consider how Assume-Gaurantee contracts could have been used for the RM paper.
The key with the RM paper, is, after the RM is set up (with the functions L, and synchronous events), the agents should learn completely on their own.
- We can replace L and this concept of synchronous events at the same time!
Assume-Gaurantee contracts for the RM paper
- Assumptions are set of trajectories with agent in starting position
- Guarantees are set of trajectories with agent eventually reaching the ending state.
- Each state+agent has it's own contract, that an RL policy must then fulfill.

LTL and RMs are interesting because they are specific examples of behavior descriptions. AGCs are more general, in that, having specified the behavior of the environment, and of the component separately, we can identify which components satisfy the contract.


# AI Problem formulations
## Consider a search and rescue problem
For a search and rescue problem, we have multi complicated sub-problems that need to be solved.
- We have to determine a function of location that denotes the probability that the target is located in an area
- We have to determine regions, and starting locations, for each of the homogeneous search operatives
	- This is the multi-agent coverage control problem. The optimal solution is non-feasible, but many heuristics can be chosen... we just have to choose an appropriate one
		- K means clustering
		- GMM clustering
		- Voronoi partitions
		- "Earth-movers problem"
- We have to determine pathing algorithms for each of the agents, that prevents collision.
	- Undoubtedly many different algorithms for this
		- Conflict based search
		- M*
		- ICTS
		- Prioritized planning
- We have to determine how the probability function changes as we search certain locations (different agents might have)
	- If we have a heterogeneous system, the coverage control problem becomes more complicated... Voronoi partitions deal with this
	- For search and rescue, a dog, for instance, can detect a human trapped in an avalanche with high probability, but cannot cover a large area. But once a dog has searched an area, we know that that area with high likelihood is empty.
For complicated systems, behavior is perhaps a series of components combined with an algorithm.

Considering what the mathematical formulations are for a problem is difficult. We have to start with: what information we have, what agents we have, what the agents can do, and break it down.

## Meeting Agenda
- Discuss motivating ideas behind AGCs, LTL
	- AGCs
		- Underlying assumption: every solution has things that need to be specified, and things that need to be performed intuitively
		- Key is composability and conjuctions, which allow for multiple levels of abstraction and unifies different requirements
	- LTL
		- Specific behavior specification language which is feasibly verifiable
	- RMs
		- Specific way of designing a system
One idea
- RMs --> AGCs --> RL


Heterogeneous capabilities... what is the best way to describe them?
- Feasibly check-able, through model checking techniques
- Expressive enough for a wide array of requirements
- Key words: heterogeneous multi-agent capability descriptors/planning
How to decompose problems into contracts automatically

Context --> What needs to be specified for task completion

What problem setting?
- Search and rescue
	- Make it bigger
	- Many different agents
		- Drones
		- Long range ground vehicles
			- Can carry and deploy drones
- What is the most general but not generic and generic
	- Literature search/chat search in seeing heterogeneous model specifications
		- Epistemic logic
			- What does the agent know? What does the human know?
		- Diantic logic
		- Coalition logic
	- We also need to be aware that the human man give a simple instruction with little context.
- Start with a simple gridworld


# 2026-05-25 Monday
Today, I would like to think about the value proposition of Assume Guarantee Contracts in the context of multi-agent learning problems.

## Cyrus Proposal Analysis

Here is what Cyrus's original proposal was:
**Project O2.a: Assume-guarantee contracts for heterogeneous agentic systems.** Engineering methodologies often rely on separation of concerns, modularity, and well-defined interfaces to build robust, complex systems out of simpler components. Assume-guarantee contracts formalize this principle for the verification of software systems. However, classical assume-guarantee frameworks were developed for static software systems and do not accommodate learning-driven components whose input-output relationships evolve dynamically with new data or with shifting inter-agent subtask boundaries. Dr. Neary’s prior work on verifiable and compositional RL and reward machines for cooperative multi-agent RL provides the technical foundation for bridging this gap, but these methods require problem decompositions to be hand-designed by an expert and rely on distinct frameworks across single- and multi-agent settings. We will address these limitations by developing a unifying framework for assume-guarantee contracts in learning-driven multi-agent systems, integrating temporal-logics, reward machines, and assume-guarantee model checking into a common representation that captures heterogeneous agent capabilities, evolving learned behaviors, and asynchronous component interactions. Next, we will use foundation models to automate the contract-generation and task-decomposition steps that currently require expert design: language and vision-language models (VLMs) will translate natural-language mission specifications into candidate decompositions, propose role assignments matched to each agent’s capabilities, and adapt these decompositions as new information is obtained throughout operation.

## Here is my understanding of what is going on:
- Assume guarantee contracts are natural, because they encode separation of concerns, modularity, and well defined interfaces, by taking these concepts as the minimal axioms for a mathematical algebra.
- The claim that assume-guarantee frameworks were developed for static software systems, or static systems (that is, the duties of each component is relatively fixed) is partially true, as they are mostly designed for conjunction of multiple views, with the underlying component being fixed.
	- In that sense, learning driven components with input output relationships evolving, or inter-agent subtask boundaries, is a new and novel requirement for assume guarantee contracts; while dynamic assume guarantee contracts (for instance, timed modular interfaces) exist, they exist on a fixed, predictable schedule and are not related to learning in this sense.
- We want to use AI to generate assume guarantee contracts automatically, without the help of a designer.

## What is the value proposition here?
- AGCs are designed to organize systems based on separation of concerns, modularity, and interfaces.
	- We don't have to do checking inside AGCs... we just have to make sure that the contracts are satisfied (so the components themselves are checked)
	- In that sense, the AGCs have to be written such that the models that represent the components are check-able.
- AGCs can be used to combine multiple contracts at once, each which has different models. This is not really new... you could formulate everything as one big contract, where the assumptions/guarantees are the union/intersection of the propositions of the separate contracts. That being said, it is not something to be sneezed at when considering requirement engineering.
- Heterogeneous systems: different modules can satisfy the same contract?
- NOVELTY: if we find a way to implement AGCs, or even modify the original formulation, such that the subtask boundaries are modular, then this may be helpful for learning problems.

#### Problems to be solved
- Asynchronous communication: how can interfaces be defined, and how should components be modeled, in such a way that this is meaningful and compactly presented?

# 2026-05-26 Tuesday
Today, I want to write out notes, and then a presentation, to summarize and document my understanding of AG contracts and how they fit into this research problem.

I will start with a brief literature review.

## Contracts for System Design
### Introduction
- Many design flaws, and expensive inefficiencies in the design process are a result of poor systems integration (especially with heterogeneous subsystems), and incomplete requirement specifications.
- There are many different ways systems are organized: platform based design and layered design, for instance. Vertical/horizontal decomposition
- A formal design algebra that allows multiple system requirements to be specified at the same time, compatible with different system frameworks, can potentially help these problems.
- "Industry has learned how to divide work. It still doesn't know how to fully describe what each divided piece assumes and guarantees"

### General Theory of Contracts
Contracts are typically described with variables, types, assumptions, and guarantees. Formally, they are defined by an implementation relation: components that implement the contract, and environments that satisfy the assumptions.
$$\mathcal{C} = (\mathcal{E}_{\mathcal{C}},\mathcal{M}_{\mathcal{C}})$$
A contract is consistent if $\mathcal{M}_{\mathcal{C}} \neq \emptyset$, and compatible if $\mathcal{E}_{\mathcal{C}} \neq \emptyset$.
The following table summarizes the theory of contracts:
![[Screenshot2026-05-26_09-30-06.png]]
The important points are
- This is a meta theory: it is not descriptive. A particular theory of contracts provides models for components, such that the models specifies the behavior required for the component to fulfill the contract and do it's part in the system. In particular, the specific implementation of a component is not specified by the theory of contracts, but rather the behavior required.
	- We can combine multiple theories of contracts for different aspects of our system, and simply take the logical conjunction (both contracts have to be satisfied for our system to work)
	- Since a given theory of contracts should be abstract enough that it does not specify an implementation, heterogeneous components that both accomplish the same behavior in different ways should be modeled such that they both fulfill the same contract.
- Typically, in a design process we will take the conjunction of multiple contracts which specify requirements for our system as a whole to create a mega contract, and then find a composition from smaller components that fulfills this mega contract. This is the design pipeline describing how this algebra is to be used.
### Specific Theories of Contracts
#### Dataflow A/G Contracts
We define an *assertion* to be:
$$ P \subseteq \Sigma \to D^* \cup D^\omega $$
Now, $\Sigma$ is the set of variables. This includes input and output variables. For example, $x, y, z$. $\Sigma \to D^* \cup D^\omega$ is the set of functions from those variables to strings of values in the domain $D$.
This represents asynchronous streams of values coming to each of the variables.
Now, in this theory of contracts, we use assertions of this form to represent both assumptions, guarantees, and components!

Formally, a contract $\mathcal{C} = (A, G)$ is a pair of assertions, and the set of environments $\mathcal{E}_{\mathcal{C}}$ are the components $E \subseteq A$. The set of components $\mathcal{M}_{\mathcal{C}}$ are the set of assertions such that $A \wedge M \subseteq G$.

For example, suppose $\Sigma =  \{ x, y, z \}$, and we are considering components that perform division $x / y = z$. The assumption might be the set $A=\{x, y, z \in \mathbb{R} : y \neq 0\}$. The guarantee might be that $G = \{ x, y, z \in R : y \neq 0, z = x / y \}$. Then, a component might be $$ M = \bigg\{ x, y, z : \begin{cases}
z = x / y  &\text{if} y \neq 0\\ z = 0 & \text{else}
\end{cases} \bigg\}$$
Then, we can see that $M \cap A = G$, as required. We can define the composition of two contracts as $G = G_{1} \wedge G_{2}$, and $A = \{  A : A \wedge G_2 \implies A_{1} \text{ and } A \wedge G_{1} \implies A_{2} \}$. The composition of two components is just the conjunction of their assertions, that is $M = M_{1} \wedge M_{2}$.
A contract restrict another contract if guarantees are identical but assumptions are relaxed. Therefore, this theory of contracts allows for composition, conjunction, restriction, and satisfaction to be checked in a clean manner.

#### Synchronous A/G Contracts
We can instead define assertions as $P \subseteq (\Sigma \to D)^* \cup (\Sigma \to D)^\omega$ to model synchronous streams of data at each variable, and introduce $\perp \in D$ in the case where a variable does not have an entry at a specific time slot. These sets of behaviors can be used to develop a theory of contracts just like dataflow A/G contracts.

#### Interface Theories
This is a much more powerful way of implementing components/contracts. The object of our attention in this case is the i/o-automaton.
- $M = (\Sigma^{\text{in}}, \Sigma^{\text{out}}, Q, q_{0}, \to)$
- $\Sigma=\Sigma^\text{in} \uplus \Sigma^\text{out}$
- $Q$ is finite, and $q_{0}$ is the initial state.
- $\to$ is a deterministic transition relation.
**Compositionality**
Composition exists when $\Sigma^{\text{out}}_{1} \cap \Sigma^{\text{out}}_{2} = \emptyset$ and then, their composition is written as $M = M_{1} \times M_{2}$, and given by
- $\Sigma^{\text{in}} = \Sigma^{\text{in}}_{1} \cap \Sigma^{\text{in}}_{2}$
- $\Sigma^{\text{out}} = \Sigma^{\text{out}}_{1} \cup \Sigma^{\text{out}}_{2}$
- $Q = Q_{1} \times Q_{2}$
- Transition relation defined for pairs $(q_{1}, q_{2}) \to^{\alpha} (q_{1}', q_{2}')$, if and only if both $q_{1} \to^{\alpha} q_{1}'$ and $q_{2} \to^{\alpha} q_{2}'$ individually. In particular, the condition that the output actions are disjoint implies that either $\alpha$ is the input to one automata and the output to another (and so does not interact with the environment, since not part of both of the automata's inputs, or that $\alpha$ is an input to both (and so interacts with the environment).
There are some details here: it may be the case that one automaton gives an output action at a certain state, where the other automaton we are composing it with does not have the matching input action. In that case, we do something called "pruning", where we remove the offending pairs of states that have such illegal mismatches of actions.
**Components and Environments**
In this case, contracts, just as components, are given by an i/o automaton. The set of environments are the set of automata that are closed (have no remaining open inputs) when composed with the contract automaton, and do not have any outputs that are not inputs of the automaton. This is quite technical, but worth understanding if you want to work with these automata.
It can be shown that there is a "biggest" environment $E_{C}$ that satisfies these conditions, where "biggest" is in the sense of "simulation", a technical concept defined in the paper. The set of components that satisfy the contract are the set of automata that compose with $E_{C}$ in a nice way that is also defined in the paper.
**Refinement**
One contract automaton refines another if, at each state, it accepts at least as many inputs, but a subset of the outputs.
**Conjunction**
There is no clean formula for the conjunction of two such contracts, unfortunately, which leads us to modal interfaces.
#### Modal Interfaces
Given $Q$ and $\Sigma$, we have two sets of transitions: those which are required, that the interface *must* implement, and those which are optional/acceptable, which the interface *may* implement. The transitions we denote $may(q)$ and $must(q)$, and we typically assume $must(q) \subseteq may(q)$. There is a lot of work that has to be done w.r.t. formalism, but then, conjunctions are defined nicely. We have that:
- $Q = Q_{1} \times Q_{2}$
- For the transition relation:
	- $must(q_{1}, q_{2}) = must_{1}(q_{1}) \cup must_{2}(q_{2})$
	- $may(q_{1}, q_{2}) = may(q_{1}) \cap may(q_{2})$
	- (Here, we are denoting this the set of of transitions originating from each of these states).
After that, some pairs may have to be pruned/processed, but this is the rough idea.
Refinement also has a nice intuitive expression:

$$\left\{
\begin{array}{rcl}
may_2(q_2) &\subseteq& may_1(q_1) \\
must_2(q_2) &\supseteq& must_1(q_1)
\end{array}
\right.
\qquad
\text{and }
\qquad
\forall \alpha \in \Sigma :
\left\{
\begin{array}{l}
q_1 \xrightarrow{\alpha}_{1} q_1' \\
q_2 \xrightarrow{\alpha}_{2} q_2'
\end{array}
\right.
\implies q_2' \preceq q_1'$$
#### Other Contract Theories
We also have timed automaton, where the available actions change at certain points in time. Typically, while time is continuous, we partition time according to the different sets of actions that are available. Then, we can reduce this to a modal interface. There is a massive zoo of such interfaces, which vary in usefulness.

## Assume Guarantee Contracts for Dynamical Systems: Theory and Computational Tools
This paper outlines an A/G theory for discrete dynamical systems described by ABCD matrices. (Denote the system $\Sigma$).
The inputs of these systems are the sequences $d \in \mathcal{S}^{n_{d}}$, and the outputs are the sequences $y \in \mathcal{S}^{n_{y}}.$
### Contract Definition
The assumptions, then, perhaps should be the set of acceptable inputs, $\mathcal{D} \subseteq \mathcal{S}^{n_{d}}$. The guarantees are tricky... sometimes, we want our output to be dependent on our input. For example, if we are doing tracking error, we will have the condition $|y - d| < \epsilon$, or something similar, which requires our restriction on the output to be a function of the input. Thus, we have that a guarantee on the behavior should be $\Omega \subseteq \mathcal{S}^{n_{d}} \times \mathcal{S}^{n_{y}}$.
### Contract Theory
- We have that a component satisfies a contract, if $\forall d \in \mathcal{D}, y \in \Sigma(d), (d, y \in \Omega)$.
- One contract refines another, denoted $\mathcal{C}_{1} \preceq \mathcal{C}_{2}$, if $\mathcal{D}_{2} \subseteq \mathcal{D}_{1}$,  and $\Omega_{1} \cap (\mathcal{D}_{2} \times \mathcal{S}^{n_{y}}) \subseteq \Omega_{2} \cap (\mathcal{D}_{1} \times \mathcal{S}^{n_{y}})$. (I.e. it accepts all and potentially more of the legal inputs, and puts out a subset of the legal outputs).
- Composition of components is defined as the composition of the two systems, in the logical, but nontrivial way. Two systems are only deemed composable if the outputs of one feed into the inputs of another (cascading the systems).
- Composition of contracts is defined as the assumptions of the input map, and using the guarantees of the output map.
- We then, have nice theories about the composition (for instance, the composition of components satisfies the composition of contracts).
### Rest of paper
They describe nice computational tools that can check of a linear system satisfies a contract. I really like this paper, because they follow the Contracts for System Design framework, making use of their abstractions appropriately and effectively.
## Assume Guarantee Reinforcement Learning
In this paper, they do not define a contract. They do not define a model for a component. They essentially do the following:
- DFA for each component, which accepts a local specification $\phi_{i}$. 
- A reward labeling function returns atomic propositions, and the policies seek to minimize the time it takes to get to the final state, where they ought always to obey the local spec. This is the "GUARANTEE" clause, that they always obey the local spec.
- The global specification, of the behavior of the entire system, is then $\wedge_{i} \phi_{i}$. 
- For each individual agent, it need only maximize its performance over the states where all the other agents are obeying their specifications. This is the "ASSUME" clause.
- They then provide results about composition of success probabilities: that is, lower bounds on the probability that the whole system makes it to their final state.
Note that they do not define models for components, or instantiate any other aspects of assume guarantee contract theory.

### Ideas for Cyrus Proposal
There are two main ideas that I would like to test, given the statement of his proposal. First, whether or not A/G contracts can be "dynamic", in that contracts, not just components, can change dynamically as a learning problem progresses.
- Can we develop a theory of contracts, such that contracts themselves evolve to redistribute sub-tasks, as reinforcement learning problems continue to learn?

Next, I want to instantiate a simple theory of heterogeneity
- A theory of contracts that is specific enough to fully encode the desired behavior, so that we have proper implementation within the system, but general enough so that agents that significantly differ in implementation can both perform.

Both of these ideas are vague and high level at this point. I will try and come up with solutions to both of them first, by coming up with a specific instantiation of the problem.

Since discrete cases are easiest to deal with, I will think about implementing a gridworld example, with multiple tasks to be completed, some of which are dependent on each other, and others which are not. Interesting! In some ways, this is an extension of the reward machine problem, because instead of designating certain tasks to a specific agent, the agents get rewarded for completing any task in any order?
- For the reward machine paper though, it seems to me that the agents were "instructed" to do a certain task by the fact that a different policy is spawned for each of it's turns in the mealy machine.
	- Certain tasks require specific assumptions... we can self-assemble components by what they can do?
	- Idea: start with the same problem as RM paper, and then compose into A/G contract with the reward i/o formulation. For each such A/G contract, start every single agent in the assumption of the policy, and see if it can learn a policy that triggers an event. If it does (randomly), then add that component to the events that it can learn. Given skills that it can do, compose the contracts such that they can be completed in total.

# 2026-06-03 Tuesday
## Distributed Systems
If you have multiple agents working towards some common goal, how can we implement global constraints and optimize a global variable, if we only have knowledge of our neighbors and cannot co-ordinate globally, that is, only using distributed controllers?
- Domain pruning algorithms remove actions which clearly don't work, to varying levels of sophistication which will be sound but may not terminate.
- Different flavors of DP problems can solve distributed optimization problems.
- In a multiagent MDP with a common reward, the global action is a vector of local actions, one for each agent. Even if the optimal Q-function is already known, choosing the optimal joint action may be hard because Q(s,a) must in principle be maximized over exponentially many combinations of local actions. Section 2.2 considers cases where the global Q-function can be represented, exactly or approximately, as a sum of local components, $Q(s,a)=\sum_iQ_{i}(s,a)$. This alone does not solve the problem, because the joint action space is still exponential. The useful additional assumption is that each $Q_{i}$​ depends only on a small subset of the agents’ action variables. Then the maximization of the global Q-function can be performed by **variable elimination**: one action variable is eliminated at a time, producing intermediate functions that summarize the best contribution of the eliminated agent conditional on the actions of the agents on which it depends. After the elimination pass computes the optimal value, a reverse pass recovers the actual maximizing joint action.
### Contract Nets
- Each agent has a cost for completing a subset of contracts, $T$. We seek the smallest cost for all the agents to complete the task.
- If we have more or equal number of agents than number of contracts, then we can give each agent his max utility contract by adjusting the "price" of the contracts for how much utility they give to the agents. That way, really popular contracts with high utility are offset, so that only the one who benefits the most can justify completing the contract.
- We can use a bidding algorithm, where you increase the price by your preference for your current choice of object each round, and add epsilon to stop deadlocks.
- Scheduling problem is where you want to complete a task which requires a certain number of time blocks of a resource to complete and you bid with your deadline and the duration. Resource the schedules you in.
### Auctions
This is a competitive environment, where multiple agents are trying to buy an item to gain utility, while spending as little money as possible. Seller wants to design a "mechanism" that leads the agents to purchase with maximal economic efficiency (the person with highest utility wins the bid and pays the utility he wants for it).
The most relevant auction types are English, Vickrey, Silent Bid, Japanese, and Dutch.
- The way we study auctions is through Bayesian games, and Bayesian mechanisms. There are a few helpful concepts/results
	- Dominant strategies means there is a strategy for every agent, such that the agent cannot improve his outcome if he changes his action
	- Bayes-Nash equilibrium: if everyone else keeps their policy the same, you cannot improve your outcome by changing your action
	- The revelation principle says that, for a given equilibrium, there is a mechanism that has the same equilibrium, where the equilibrium point results from everybody being truthful. However, we cannot guarantee other equilibrium points don't exist, or which equilibrium point we will arrive at.
	- Risk neutral/averse/seeking deals with how much utility you assign to different amounts of money, and will affect your quasi linear utility.
- Expected revenue is the same by revenue equivalence theorem if the valuations are drawn IVP from a CDF F which is atomless and has support v >= 0, and the mechanism is efficient, and the agents are all risk neutral.
### Multi Unit Auctions
- If each person wants one unit, you can have a truthful mechanism if you assign the price of the highest bidding loser to everyone.
- For bids with people bidding with different bids each with multiple units and prices, you need to do an optimization problem to determine who wins. You can also set this up in a VGC way so that truthfulness is optimal.
### Combinatorial Auctions
- In this case, every single subset of objects has it's own value, with interesting relationships between the valuations of different subsets.
	- We usually assume the empty set has valuation 0, and "free disposal" means the valuation of a set is greater or equal to the price of any of its subset.
- You have to solve an optimization problem in order to determine who gets what (winner determination problem)
- You have to think about how to describe bids, rather than naming a valuation on each of the $2^{|O|}$ subsets of objects. Using atomic valuations, where a price of 0 is assigned to every subset except for 1 that you want (as well as all of its supersets), and then combining these with OR and XOR operations is one way of doing this.
	- We need valuation and verification operations to be quick, and also need as few "words" in common expressions as possible.
- Indirect mechanism: instead of asking everyone for their valuation functions, you can simply query what you need to solve your WDP.

## Contract Assignment Problem
For my problem, I need a way to assign contracts. Every single agent will have a specific amount of time required to do a contract. We are trying to minimize the total completion time.
### Static Allocation
First, I want to start by brainstorming different considerations.
- If one agent can do everything well, and another agent cannot, then, similar to the contract net auction like scenario in chapter 2, we want to distribute such that each agent has at least one task, and the sum of the utilities is maximized.
- In what sense are thinking about "utility" in this scenario? 
	- The makespan/resources it takes to complete the task? 
		- This is difficult, because we don't know about the sequence of the tasks.
	- We could think about other resources, such as fuel, or compute; or does this complicate the matter? 
	- *In the learning context, perhaps we could optimize for consistency/success rate?*
- What reason would we have for not putting the best performing agent on every task?
	- Maybe we can!
	- We might have the case where different agents are "contracted" to different physical locations in their collaboration.
		- Then, each agent can choose between different sets of tasks at different locations that they need to be allocated to.
		- What if these constraints only hold to certain tasks? So you can do more than one task in one location, but you cannot do more than one task in another location?
		- Is there a science behind auctions that look like this? These look like optimization constraints.
- What about cases where you need different agents on different contracts, but your evaluation depends on the assortment of who uses which contract? For example, even though two different pairs of agents solve 2 different contracts which depend on each other, one pair has a higher success rate than the other pair.
	- In this case, we will have pairwise terms in the assortment problem's objective function, but this will quickly become difficult, so I will ignore this for now.

I thought about these things, and came to the following conclusion:
- We solve a makespan optimization problem, which reduces the amount of time it takes for the group of agents to solve the problem. That is, if agent $i$ takes $\tau_{i, k}$ time steps to solve contract $k$, we solve $$
\min \sum_{i, k} \tau_{i, k} x_{i,k}
$$ where we have $$
\sum_{i} x_{i, k} = 1
$$ so that each contract is assigned once. Problem: what about precedence? When different contracts need other contracts to have been completed first? What if there are separate "precedence graphs" for different subtasks that get doubly assigned, causing delays as an agent in both tasks completes one task first as the other waits?
### Online Contract
- Perhaps, we can solve this problem online instead, and maybe even set it up so that it performs very well in comparison to an optimal scheduler. In particular, we could have the following heuristic
	- The currently "active" contracts (the ones with their assumptions satisfied) are presented to the scheduling algorithm.
	- Every single agent is listed, with the amount of time that it would take them to complete the next task, plus how long we are expecting for them to complete their previous task.
	- We then assign tasks in such a way that total time is minimized.
	- We seek to minimize the makespan, so we take the time it takes for the final agent to complete their task.
	- Isn't this like a queuing problem? Every agent is a queue and we are seeking to minimize the length of the longest queue? Can this be formulated in terms of price/utility so that 
	- If you wait longer for previous contracts to be completed, and do "batch scheduling" then you may get a more optimal assignment. However, the wait time wastes time.
- How do we know which agents *can* do a given contract? What if we have decisions to make, about where to dispatch agents? We can forgo this decision for now, and just assume that each contract has learned what it can and cannot do globally. We can have some threshold $p_{min}$ which is the success probability, and then have expected time of completion as the ultimate criterion.
### Verdict
Let $S_{1}$ be the set of contracts that are available at $t=0$. Solve a scheduling problem, such that the completion time for all of the available contracts is as soon as possible. Next, consider the set of contracts $S_{2}$, which are available once all the contracts in $S_{1}$ are done running. Solve another similar scheduling problem, with the nuance that we have to add the availability time of the next contract based on the previous scheduling decision, to determine when the next problem will be completed.

To solve this problem optimally, we would have to solve a DP problem. But this should be simpler/faster I think.


# 2026-06-04 Thursday
## Meeting
One way of solving contract assignment problem is through a centralized approach
Some oracle is able to give the contracts to everyone, and he thinks about the whole tasks. 
If you think about it as a distributed approach.
How do you set a bidding process up? In a way that is good, and nice, but is decided in 

Credit assignment through assume guarantee contracts

Use the value function of the RL problem (if you used a sparse reward in order to solve the problem) for your contract utility

Have one agent who is building the whole thing.
- He sees everything he has already, and he is the one who auctions for a contract which is still required.
	- All the other agents get that signal.
	- Marketplace where agents are talking.
	- The issue is: making sure the actual task is being completed.
	- The planner agent: his task is able to say when a contract is needed actually to complete the whole task, and the whole overarching task.
	- Competition makes prices less for a given contract.
	- Which contracts are worth completing, to compete with a learning.