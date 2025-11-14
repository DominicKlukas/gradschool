
from typing import List, Tuple
import numpy as np
import gymnasium as gym
from gridworld_mdp import GridworldMDP

Coord = Tuple[int, int]  # (row, col)

class GridworldEnv(gym.Env):
    """
    Gymnasium environment wrapper for GridworldMDP.
    """

    metadata = {'render_modes': ['human', 'ansi'], 'render_fps': 4}

    def __init__(
            self, 
            height: int,
            width: int,
            init: Coord,
            goal: Coord,
            sink: Coord | None = None,
            wall: Coord | List[Coord] | None = None,
            reward_goal: float = +1.0,
            reward_sink: float = -1.0,
            step_cost: float = -0.1,
            slip_p: float = 0.3,
            discount : float = 0.99,
            reward_depends_on_next : bool = False,
        ):
        """
        Initialize the Gridworld Gym environment.
        """
        super().__init__()

        # Create the underlying MDP
        self.mdp = GridworldMDP(
            height=height,
            width=width,
            init=init,
            goal=goal,
            sink=sink,
            wall=wall,
            reward_goal=reward_goal,
            reward_sink=reward_sink,
            step_cost=step_cost,
            slip_p=slip_p,
            discount=discount,
            reward_depends_on_next=reward_depends_on_next,
        )

        # TODO: Define action and observation spaces and expose nS and nA
        self.state = self.mdp.init
        self.nS = self.mdp.nS
        self.nA = self.mdp.nA
        

    def reset(self, seed=None, options: dict = None):
        """
        Reset the environment to the initial state.
        Arguments:
                options: "state", integer in [0, nS), determines the starting state
        Returns:
          obs: the observation corresponding to the reset initial state 
            (in this case just return the initial state index itself)
          info: additional info (empty dict in this case)
        """
        if options is not None:
            self.state = options["state"]
        else:
            self.state = self.mdp.init

        observation = self.state
        info = {}
        return observation, info

    def step(self, action):
        """
        Take an action in the environment.
        Arguments:
            action: the action to take (integer in [0, nA-1])
        Returns:
          next_state: the next state after taking the action
          reward: the reward received
          done: whether the episode has ended
          info: additional info (empty dict here)
        """
        # TODO: Implement step method (hint, make use of self.mdp.p(state, action))
        # Get the transitions for the state action pair
        transitions = self.mdp.P(self.state, action)

        # Choose the transition
        probabilities = np.array([t.prob for t in transitions])
        probabilities = probabilities/np.sum(probabilities)
        chosen_transition = np.random.choice(transitions, p=probabilities)

        # Get the results
        next_state = chosen_transition.next_state
        self.state = next_state
        reward = chosen_transition.reward
        done = chosen_transition.done
        info = {}
        return next_state, reward, done, info
