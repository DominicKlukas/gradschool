import numpy as np
import matplotlib.pyplot as plt
import gymnasium as gym

from homework_3_helpers import get_optimal_Q_V_and_policy
from gridworld_gym_env import GridworldEnv

######### MC Prediction (First-Visit) code #########
def generate_episode(env, policy, max_steps: int = 1000):
    """
    Roll out one episode using the given policy.
    Returns:
        states:  list of observations (tuples) per time step
        actions: list of actions taken per time step
        rewards: list of rewards per time step
    """
    # TODO: Implement generate_episode function
    states = [env.state]
    actions = []
    rewards = []
    step = 0
    if env.mdp.is_absorbing(env.state):
        return states, actions, rewards
    while step < max_steps:
        action = np.argmax(policy[env.state])
        next_state, reward, done, info = env.step(action)
        states += [next_state]
        actions += [action]
        rewards += [reward]
        step += 1
        if done:
            break
    return states, actions, rewards

def mc_prediction_first_visit(
    env,
    policy,
    num_episodes: int = 500000,
    gamma: float = 1.0,
):
    """
    Monte-Carlo prediction (first-visit) to estimate V^pi.
    Args:
        env: Gym environment
        policy: function mapping state -> action
        num_episodes: number of episodes to sample
        gamma: discount factor
    Returns:
        V_list: list of V arrays (numpy arrays of dimension (env.nS)) at the start of each episode.
        N_list: list of N arrays (numpy arrays of dimension (env.nS)) at the start of each episode.
    """
    # TODO: Implement mc_prediction_first_visit function
    num_eps_per_state = int(num_episodes / env.nS)
    N_list = []
    V_list = []
    N_s_list = np.zeros(env.nS)
    for s in range(env.nS):
        V_s_list = []
        V_s = 0
        for i in range(num_eps_per_state):
            env.reset(options={"state": s})
            states, actions, rewards = generate_episode(env, policy)
            for st in states:
                N_s_list[st] += 1 # This implies that we are interested in the 
                        # total number of visits over all the Monte-Carlo runs
            discounts = gamma ** np.arange(len(rewards))
            G_i = np.sum(discounts * rewards)
            V_s += (G_i-V_s) / (i + 1)
            V_s_list += [V_s]
        V_list.append(V_s_list)
        N_list.append(N_s_list.copy())

    # Transform shape to (num_eps_per_state,nS)
    V_list = np.array(V_list).T
    N_list = np.array(N_list)
    return V_list, N_list

def plot_RMSE(V_list):

    num_episodes_per_state = len(V_list)
    RMSE = []
    for i in range(num_episodes_per_state):
        RMSE += [np.linalg.norm(V_list[i] - V_optimal)]
    plt.figure(figsize=(6, 4))
    plt.plot(range(num_episodes_per_state), RMSE, label='RMSE', color='blue')
    plt.xlabel('Episode Number')
    plt.ylabel('RMSE at Episodes')
    plt.title('Root Mean Squared Error, V_mc vs V*')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.plot(RMSE)
    plt.show()

if __name__ == "__main__":

    gamma = 0.9

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
    #env.mdp.plot_grid()
    #env.mdp.plot_values(V_optimal, annotate=True)
    #env.mdp.plot_policy(policy_optimal)

    ############ Monte-Carlo Prediction experiment ###########  
    # TODO: Implement the code to answer the homework questions.
    num_episodes = 10000
    V_list, N_list = mc_prediction_first_visit(env, policy_optimal, num_episodes, gamma)

    V_mc_final = V_list[-1]

    env.mdp.plot_values(np.abs(V_mc_final - V_optimal), annotate=True)
    env.mdp.plot_values(N_list[-1], annotate=True)
    plot_RMSE(V_list)
