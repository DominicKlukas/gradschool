import numpy as np
from gridworld_gym_env import GridworldEnv

import matplotlib.pyplot as plt

from homework_3_helpers import get_optimal_Q_V_and_policy

def q_learning(
    env: GridworldEnv,
    num_episodes: int,
    alpha: float,
    gamma: float = 1.0,
    epsilon: float = 0.1,
):
    """
    Q-Learning algorithm to learn optimal action-value function Q and policy.
    Args:
        env: Gym environment
        num_episodes: number of episodes to sample
        alpha: step-size parameter
        gamma: discount factor
        epsilon: probability of choosing a random action (epsilon-greedy)
    Returns:
        Q_list: list of Q arrays (numpy arrays of dimension (env.nS, env.nA)) at the start of each episode.
        N_visit_list: list of N_visit arrays (numpy arrays of dimension (env.nS)) at the start of each episode.
    """

    Q_list = [] # to store a copy of Q at the start of each episode
    N_visit_list = [] # to store a copy of N_visit at the start of each episode

    Q = np.zeros((env.nS, env.nA), dtype=np.float64) # action-value function estimate
    N_visit = np.zeros(env.nS, dtype=np.int32) # state visit counts

    def policy(Q_p, s, eps):
        nA = Q_p.shape[1]
        if np.random.random() < eps:
            return np.random.randint(nA)
        else:
            return np.argmax(Q_p[s])
    length = 0
    for _ in range(num_episodes):
        Q_list.append(Q.copy())
        N_visit_list.append(N_visit.copy())
        env.reset() 
        done = False
        state = env.state
        states = [state]
        if _ %1000 == 0:
            print(f"We are at {_} with average episode length {length}", flush=True)
            length = 0
        length_ep = 0
        while not done:
            N_visit[env.state] += 1
            action = policy(Q, env.state, epsilon)
            next_state, reward, done, info = env.step(action)
            Q[state, action] += alpha*(reward + gamma*np.max(Q[next_state, :]) - Q[state, action])
            states += [env.state]
            state= env.state

            #For Logging
            length_ep += 1
        length += (length_ep - length)/(_ - (_/1000)*1000 + 1)
    return Q_list, N_visit_list

if __name__ == "__main__":
    # Environment parameters
    gamma = 0.95
    epsilon = 0.1

    # Construct the MDP instance    
    env = GridworldEnv(
        height=6,
        width=9,
        init=(2, 0),
        goal=(0, 8),
        sink=(5, 8),
        wall=[(1, 2), (2, 2), (3,2), (4,5), (0, 7), (1,7), (2,7)],
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

    # Q-Learning experiment

    alpha_list = [0.01, 0.05, 0.15] # different learning rates to try
    num_episodes = 10000

    # TODO: Implement answers to homework problems.
    def RMSE_calculator(V_n, V_optimal):
        return np.sqrt(np.mean((V_n - V_optimal)**2))


    rmse_list = []
    n = np.arange(1, num_episodes+1)
    for alpha in alpha_list:
        Q_list, N_visit_list = q_learning(env,num_episodes,alpha,gamma,epsilon)
        V_list = [np.max(q, axis=1) for q in Q_list]
        rmse = np.array([RMSE_calculator(v, V_optimal) for v in V_list])
        plt.plot(n, rmse, label=f"alpha={alpha}")
    plt.legend()
    plt.show()
