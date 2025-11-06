import numpy as np
from gridworld_gym_env import GridworldEnv
import random

import matplotlib.pyplot as plt

from homework_3_helpers import get_optimal_Q_V_and_policy

def dyna_q(
    env,
    num_episodes: int,
    alpha: float,
    n_planning_steps: int,
    gamma: float = 1.0,
    epsilon: float = 0.1,
):
    """
    Dyna-Q algorithm to learn optimal action-value function Q and policy.
    Args:
        env: Gym environment
        num_episodes: number of episodes to sample
        alpha: step-size parameter
        n_planning_steps: number of planning steps per real step
        gamma: discount factor
        epsilon: probability of choosing a random action (epsilon-greedy)
    Returns:
        Q_list: list of Q arrays (numpy arrays of dimension (env.nS, env.nA)) at the start of each episode.
    """

    Q_list = []

    Q = np.zeros((env.nS, env.nA), dtype=np.float64)

    model = {}   # (s,a) -> list of (r, s_next, done)
    seen_keys = []

    def policy(Q_p, s, eps):
        nA = Q_p.shape[1]
        if np.random.random() < eps:
            return np.random.randint(nA)
        else:
            return np.argmax(Q_p[s])
    length = 0
    for _ in range(num_episodes):
        Q_list.append(Q.copy())
        env.reset() 
        done = False
        state = env.state
        
        # logging code
        if _ %1000 == 0:
            print(f"We are at {_} with average episode length {length/1000}", flush=True)
            length = 0
        length_ep = 0

        while not done:
            action = policy(Q, env.state, epsilon)
            next_state, reward, done, info = env.step(action)
            Q[state, action] += alpha*(reward + gamma*np.max(Q[next_state, :]) - Q[state, action])

            if (state, action) not in model:
                seen_keys.append((state,action))
            model[(state, action)] = (reward, next_state, done)

            state = env.state
            for i in range(n_planning_steps):
                key = random.choice(seen_keys)
                state_p, action_p = key
                reward_p, next_state_p, irrelevant = model[key]
                Q[state_p, action_p] += alpha*(reward_p + gamma*np.max(Q[next_state_p, :]) - Q[state_p, action_p])

            # Logging Code
            length_ep += 1
        length += length_ep

    return Q_list

if __name__ == "__main__":
    # Environment parameters
    gamma = 0.9
    epsilon = 0.1

    # Construct the MDP instance
    env = GridworldEnv(
        height=6,
        width=9,
        init=(2, 0),
        goal=(0, 8),
        sink=(5, 8),
        wall=[(1, 2), (2, 2), (3,2), (4,5), (0,7), (1,7), (2,7)],
        reward_goal=+1.0,
        reward_sink=-1.0,
        step_cost=-0.1,
        slip_p=0.05,  # 5% chance to slip,
        discount=gamma,
    )
    
    # Compute optimal Q, V, and policy via Q-iteration for comparison with your RL-based results.
    Q_optimal, V_optimal, policy_optimal = get_optimal_Q_V_and_policy(env.mdp, max_iter=10000, tol=1e-6)
    
    # Sanity check: visualize the MDP, optimal value function, and optimal policy
    env.mdp.plot_grid()
    env.mdp.plot_values(V_optimal, annotate=True)
    env.mdp.plot_policy(policy_optimal)

    # Dyna-Q experiment
    n_list = [0, 5,50] # different n_planning_steps to try
    alpha = 0.15
    num_episodes = 500


    # TODO: Implement answers to homework problems.
    def RMSE_calculator(V_n, V_optimal):
        return np.sqrt(np.mean((V_n - V_optimal)**2))


    rmse_list = []
    n = np.arange(1, num_episodes+1)
    for n_planning in n_list:
        Q_list = dyna_q(env, num_episodes, alpha, n_planning, gamma, epsilon)
        V_list = [np.max(q, axis=1) for q in Q_list]
        rmse = np.array([RMSE_calculator(v, V_optimal) for v in V_list])
        plt.plot(n, rmse, label=f"n_plan={n_planning}")
    plt.legend()
    plt.show()
