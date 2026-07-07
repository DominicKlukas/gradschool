## Slides
1. Recent AI systems can take our robotics systems to the next level. RL for control, planning, understanding of the world for our LLMs, etc.
2. One specific robotics systems is a multi-agent system. They face the following problems:
	1. The curse of dimensionality
	2. Communication
3. Solution to these problems
	1. Instead of solving a problem end to end, break the problem down subtasks which can then be solved as individual learning problems.
	2. At this point, we may ask ourselves: is this not just a regular systems design problem? How can we us traditional formal systems techniques to help us to design reliable systems?
______
1. Classical problems that industry systems designers face
		1. You optimize for one specification, and then you continually iterate until all of your requirements are satisfied.
		2. You always struggle at the integration phase, which causes you to go back to the drawing board, over and over again.
		3. We need a way to explicitly write out systems requirements.
			1. If humans need to do this, how much more, if we want self assembling autonomous systems, need a way of explicitly writing out systems requirements!
2. In response to those problems, Beneviste et al. published a moderately influential monograph, which attempted to distill the key elements of different systems design elements, which represents components, subsystems, and systems in such a way that keeps track of requirements, compatibility between components.
	1. To motivate this theory of contracts, I will do so step by step, building up the motivations for the mathematical objects, and their properties, step by step.
	2. Start with a component. A component is just a part of your system. It can be a single part, or a collection of parts that forms a subsystem that goes into your system.
	3. Next, we need some way to represent the properties of the component. This could be a list of inputs and outputs, a linear map, or some sort of state machine, that describes the behavior of the component.
	4. Next, we have to be able to say which components are composable, and which ones are not.
	5. An environment for a component is a component such that it is defined and closed.
	6. Contracts specify a set of assumptions that the environment must grant, and the guarantees that, if the environment is doing it's job, the component must satisfy.
		1. We can talk about refinement of contracts.
3. Next, I want to talk about my research, and how I intend to use these ideas to specifically for learning in the context of multi-agent heterogeneous systems.
	1. Heterogeneous is in the context of different state/action spaces.
	2. Here, I specify a component by it's MDP, which indicates the dynamics of the system.
	3. The contracts are specified by so-called i/o automata.
	4. What I already proved:
		1. While contract theory does not say much about how contracts can be broken down, it does say something something about how contracts can be composed.
		2. I proved that, given an automaton, where every action can be specified by it's source (so you relabel with an automaton where every action is specified by a single output), you can decompose it into the m automata with at most 6 states, and 4 states if you have a shared goal state.
		3. I am in the process of formalizing MDPs as components (so, defining which MDPs are composable, when they satisfy a contract).
		4. This will then be a valid use of contract theory: we specify a contract (high level states that lead to task completion), and then assign MDPs based on which agents are available/how well they can learn different tasks.