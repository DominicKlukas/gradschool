
Start with a brief literature review.
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

Formally, a contract $\mathcal{C} = (A, G)$ is a pair of assertions,

The set of environments $\mathcal{E}_{\mathcal{C}}$ are the components $E \subseteq A$. 
The set of components $\mathcal{M}_{\mathcal{C}}$ are the set of assertions such that $A \wedge M \subseteq G$.

For example, suppose $\Sigma =  \{ x, y, z \}$, and we are considering components that perform division $x / y = z$. The assumption might be the set $A=\{x, y, z \in \mathbb{R} : y \neq 0\}$. The guarantee might be that $G = \{ x, y, z \in R : y \neq 0, z = x / y \}$. Then, a component might be $$ M = \bigg\{ x, y, z : \begin{cases}
z = x / y  &\text{if} y \neq 0\\ z = 0 & \text{else}
\end{cases} \bigg\}$$
Then, we can see that $M \cap A = G$, as required. 

Composition of two contracts:

$G = G_{1} \wedge G_{2}$, and $A = \{  A : A \wedge G_2 \implies A_{1} \text{ and } A \wedge G_{1} \implies A_{2} \}$. 

The composition of two components is just the conjunction of their assertions, that is $M = M_{1} \wedge M_{2}$.

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
- Transition relation defined for pairs $(q_{1}, q_{2}) \to^{\alpha} (q_{1}', q_{2}')$, if and only if both $q_{1} \to^{\alpha} q_{1}'$ and $q_{2} \to^{\alpha} q_{2}'$ individually. 
	- Either $\alpha$ is an input for both, or input for one, output for the other.
There are some details here: it may be the case that one automaton gives an output action at a certain state, where the other automaton we are composing it with does not have the matching input action. In that case, we do something called "pruning", where we remove the offending pairs of states that have such illegal mismatches of actions.
**Components and Environments**
In this case, contracts, just as components, are given by an i/o automaton. The set of environments are the set of automata that are closed (have no remaining open inputs) when composed with the contract automaton, and do not have any outputs that are not inputs of the automaton. This is quite technical, but worth understanding if you want to work with these automata.
It can be shown that there is a "biggest" environment $E_{C}$ that satisfies these conditions, where "biggest" is in the sense of "simulation", a technical concept defined in the paper. The set of components that satisfy the contract are the set of automata that compose with $E_{C}$ in a nice way that is also defined in the paper.
**Refinement**
One contract automaton refines another if, at each state, it accepts at least as many inputs, but a subset of the outputs.
**Conjunction**
There is no clean formula for the conjunction of two such contracts. But for modal interfaces, there are!
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
	- Consider the RM paper. What if, instead of treating it as an RM, write it as a contract, written as an i/o interface, and we find the finest resolution interface that we can. Then, we run each of the agents, and see if they can learn to complete any task. If it does, we add a policy to that agent, and train this new policy to complete that subcontract, by treating the decomposed contract unit as an RM (where the assumptions hold and the agent then learns to complete the task). Once we have each agent having been learned by one contract, we take the best performing agent on each contract, and compose them to solve the entire task.


### Chat Transcript for Developing Experiments
I would make the experiments deliberately modest and diagnostic. The paper’s experimental claim should not be “we beat MARL,” but rather: given a high-level automaton contract, decomposed into atomic subtasks, learned component performance can be used to assign contracts to heterogeneous agents, and the composed assigned components then satisfy the original task more reliably, cheaply, or flexibly than hand-fixed or structure-free alternatives. That matches the contribution in your draft: reward machines/i-o automata are the contracts, MDPs are the satisfying components, and the assignment mechanism chooses which component should satisfy which contract under capability and availability constraints.

The closest existing pressure point is that prior RM-for-cooperative-MARL work already uses reward machines to encode a team task and decompose it into agent-level subtasks; your difference should be that the agent-subtask mapping is not merely designed into the projected RMs, but emerges from contract satisfaction estimates plus assignment constraints. ([arXiv](https://arxiv.org/abs/2007.01962?utm_source=chatgpt.com "Reward Machines for Cooperative Multi-Agent ...")) More recent RM-MARL work also emphasizes hierarchical decomposition and concurrency, so your experiments should avoid competing on “deep MARL sophistication” and instead isolate the cleaner systems point: contracts are substitutable behavioral specifications, and learned MDP components can be swapped into those specifications. ([arXiv](https://arxiv.org/abs/2403.07005?utm_source=chatgpt.com "Multi-Agent Reinforcement Learning with a Hierarchy of Reward Machines"))

For the simple pressure-plate chess-piece task, make it a sanity-check experiment, not a benchmark. Use a small deterministic or lightly stochastic gridworld with two to four agents, three to six atomic contracts, and an automaton that is simple enough to draw in the paper. PressurePlate-style environments are already recognizable in MARL as cooperative sparse-reward gridworlds where agents unlock progression by standing on assigned plates, so the reader will understand the task quickly. ([IFAAMAS](https://www.ifaamas.org/Proceedings/aamas2025/pdfs/p1613.pdf?utm_source=chatgpt.com "An Extended Benchmarking of Multi-Agent Reinforcement ...")) Your variant should add heterogeneity: for example, rook-agents move efficiently along corridors, knight-agents can jump one-cell walls, bishop-agents pass diagonal cracks, and pawn-agents are slow but can hold plates cheaply. The global task could be: open door A, move a key carrier through a crack corridor, keep plate B depressed while another agent crosses, jump a wall to reach a switch, then deliver a token to the goal. The RM has one transition per high-level event, and each event becomes a contract: `hold_plate_A`, `cross_crack`, `jump_wall`, `carry_key`, `activate_switch`, `deliver_goal`.

The key engineering detail is that every contract should have more than one eligible agent, but not equally good agents. This is what makes assignment meaningful. Do not make the knight the only agent physically capable of `jump_wall`, because then the contract assignment becomes trivial. Instead, make the knight complete it in 6 expected steps, the rook complete it by a long detour in 18 steps, and the pawn complete it only with low probability or high battery cost. Then the assignment problem is not binary feasibility but learned quality-of-satisfaction. For each agent-contract pair, estimate success probability, expected duration, and expected return after a fixed training budget. Then solve a small assignment problem over those estimates. In the paper, this gives you a clean table: rows are contracts, columns are agents, entries are learned costs/successes, and the chosen assignment is visible.

For this first task, I would use tabular Q-learning or a very small neural method, not MAPPO/QMIX. The goal is interpretability and reproducibility. Reward machines were originally useful partly because they decompose temporally extended rewards into structured subproblems, and QRM-style learning has a clear tabular story; leaning on that style keeps the first experiment close to the theory. ([Proceedings of Machine Learning Research](https://proceedings.mlr.press/v80/icarte18a.html?utm_source=chatgpt.com "Using Reward Machines for High-Level Task Specification ...")) Report learning curves, but the most important figure is probably not the curve. The most important figure is a four-panel schematic: global RM, decomposed atomic contracts, learned agent-contract capability matrix, and final composed assignment executing the task.

For the warehouse task, resist the temptation to build a full logistics simulator. Use a warehouse-shaped gridworld, but make the symbolic structure richer than the pressure-plate example. Existing RWARE-style environments already simulate robots moving shelves to workstations in a grid warehouse, and they are familiar in MARL as cooperative, partially observable warehouse tasks. ([GitHub](https://github.com/semitable/robotic-warehouse?utm_source=chatgpt.com "Multi-Robot Warehouse (RWARE): A ...")) PettingZoo is also a reasonable API target because it explicitly supports multi-agent RL environments, including simultaneous-action settings through its Parallel API. ([PettingZoo](https://pettingzoo.farama.org/index.html?utm_source=chatgpt.com "PettingZoo Documentation")) You can implement your environment from scratch while borrowing the conceptual shape: shelves, stations, chargers, regions, and robots with heterogeneous capabilities.

A good warehouse automaton might be order-centric: `receive_order → retrieve_shelf → bring_to_station → inspect_or_pack → deliver_bin → return_shelf → recharge_if_needed → complete_order`. Then add branching and constraints. Some shelves are heavy and require either one heavy robot or two small robots. Some items are fragile and require a slow route. Some stations are region-specific. Some robots cannot enter cold-storage regions. Some robots have limited battery. Some contracts must be grouped, such as `retrieve_shelf` and `return_shelf`, because assigning them to different robots creates wasteful handoff behavior. Some contracts are mutually exclusive for the same robot because of locality or battery. This directly exercises the “contract constraints” section of your draft.

The warehouse experiment should have three difficulty levels rather than one large setting. Level 1: two robots, two shelves, one station, no charging. Level 2: four robots, four to six shelves, two stations, heterogeneous abilities. Level 3: six to eight robots, battery/charging, regional constraints, and stochastic order arrivals. This lets you show scaling in a controlled way without claiming a general solution to warehouse MARL. If you use a standard library scaffold, Minigrid is a reasonable reference point for lightweight, customizable gridworld construction, while PettingZoo gives you a multi-agent API convention. ([MiniGrid](https://minigrid.farama.org/index.html?utm_source=chatgpt.com "MiniGrid Documentation"))

The experimental baselines should be few and conceptually sharp. I would use: fixed manual projected-RM assignment, random feasible assignment, capability-only assignment, oracle assignment, and no-contract MARL. The fixed manual baseline represents the existing projected-RM design burden. The random feasible baseline shows that contracts alone are not enough; assignment quality matters. The capability-only baseline uses hand-coded eligibility but no learned performance estimates. The oracle assignment is computed by exhaustive evaluation in the small task and approximated in the warehouse task; it gives an upper bound, not a competitor. The no-contract MARL baseline is there only to show why the structured task representation matters, not to claim superiority over all MARL methods. Current MARL benchmarking papers repeatedly note that cooperative MARL evaluation is fragile and benchmark-dependent, so keeping baselines focused will make the paper less vulnerable to reviewer complaints about algorithm selection. ([OpenReview](https://openreview.net/forum?id=cIrPX-Sn5n&utm_source=chatgpt.com "Benchmarking Multi-Agent Deep Reinforcement Learning ..."))

The most important ablations are assignment ablations, not neural-network ablations. Remove learned costs and use only binary feasibility. Remove grouping constraints. Remove communication/listening constraints and let every agent observe every high-level event. Remove contract decomposition and use one monolithic global RM. Remove reassignment and force the first chosen assignment for the whole run. Then add one “substitutability” test: after training, disable the best robot for one contract and show that the assignment procedure can select the next-best satisfying component without redesigning the RM. That test is probably the cleanest experimental expression of the contract-theory idea.

For metrics, report both RL metrics and contract metrics. RL metrics: success rate, return, sample efficiency measured by area under the learning curve, and steps-to-completion/makespan. Contract metrics: contract satisfaction rate per subtask, composed-task satisfaction rate, number of violated assumptions, number of emitted high-level events, and communication events per episode. Assignment metrics: learned assignment cost, regret to oracle on small instances, reassignment frequency, and solver/runtime overhead. In the warehouse task, include throughput, average order completion time, battery failures, station idle time, and robot utilization. This makes the experiment read like a systems paper with RL components, rather than an RL paper with some formal language on top.

A clean experimental pipeline would be: first define the global RM; second decompose it into atomic contracts; third train or evaluate each eligible agent-contract component in isolated local environments; fourth build a capability/cost matrix; fifth solve the constrained assignment; sixth compose the selected components and run end-to-end episodes in the full gridworld. For every reported result, keep the RL algorithm fixed across methods unless the method definition forces a change. This matters because otherwise reviewers may attribute performance to PPO/QMIX tuning rather than to contracts. If you need deep RL in the warehouse setting, use a standard independent learner or shared-parameter PPO-style setup, but present it as an implementation detail.

I would design the first figure of the experimental section as a conceptual figure, not a result: “from RM to contracts to learned component costs to assignment to execution.” The second figure should be the simple pressure-plate result: learning curves plus assignment matrix. The third figure should be the warehouse result: throughput or success versus environment complexity. The fourth figure should be the substitutability/failure result: remove a robot, compare no reassignment, random reassignment, and contract-based reassignment. That final figure will probably sell the idea best.

The minimum publishable experimental package, in my view, is therefore: one small pressure-plate chess-piece gridworld with exhaustive oracle comparison; one warehouse gridworld with three scales; five baselines; four ablations; and one failure/reassignment study. That is enough to support the paper’s actual claim. Adding LLM agents, human interaction, or fixed controllers should stay as illustrative future work unless you already have a very clean implementation, because those could distract from the main mathematical contribution.