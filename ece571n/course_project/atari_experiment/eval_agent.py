# eval_agent.py
import os, numpy as np, torch, torch.nn as nn
import gymnasium as gym
from torch.distributions.categorical import Categorical
from dataclasses import dataclass
import tyro
import ale_py                      # ensure ALE envs are registered
import matplotlib.pyplot as plt

# ---- wrappers (same as training) ----
from atari_wrappers import ClipRewardEnv, EpisodicLifeEnv, FireResetEnv, MaxAndSkipEnv, NoopResetEnv, CropScoreboard


def layer_init(layer, std=np.sqrt(2), bias_const=0.0):
    torch.nn.init.orthogonal_(layer.weight, std)
    torch.nn.init.constant_(layer.bias, bias_const)
    return layer

class Agent(nn.Module):
    def __init__(self, action_n: int):
        super().__init__()
        self.network = nn.Sequential(
            layer_init(nn.Conv2d(4, 32, 8, stride=4)), nn.ReLU(),
            layer_init(nn.Conv2d(32, 64, 4, stride=2)), nn.ReLU(),
            layer_init(nn.Conv2d(64, 64, 3, stride=1)), nn.ReLU(),
            nn.Flatten(),
            layer_init(nn.Linear(64 * 7 * 7, 512)), nn.ReLU(),
        )
        self.actor  = layer_init(nn.Linear(512, action_n), std=0.01)
        self.critic = layer_init(nn.Linear(512, 1), std=1)

    @torch.no_grad()
    def act(self, obs_t):
        h = self.network(obs_t / 255.0)
        return self.actor(h).argmax(dim=-1)


def make_env(env_id, render):
    if render:
        env = gym.make(env_id, render_mode="human")
    else:
        env = gym.make(env_id)
    env = gym.wrappers.RecordEpisodeStatistics(env)
    env = NoopResetEnv(env, noop_max=30)
    env = MaxAndSkipEnv(env, skip=4)
    env = EpisodicLifeEnv(env)
    if "FIRE" in env.unwrapped.get_action_meanings():
        env = FireResetEnv(env)
    env = ClipRewardEnv(env)
    print(env.observation_space.shape)
    env = CropScoreboard(env)
    env = gym.wrappers.ResizeObservation(env, (84, 84))
    print(env.observation_space.shape)
    env = gym.wrappers.GrayscaleObservation(env)
    env = gym.wrappers.FrameStackObservation(env, 4)
    return env


@dataclass
class Args:
    weights: str = "/home/dominic/logs/ppo_breakout_final.pt"
    """Path to saved model weights (.pt)"""
    env: str = "ALE/Breakout-v5"
    """Gym environment ID"""
    episodes: int = 3
    """Number of episodes to run"""
    cuda: bool = False
    """Use GPU if available"""
    render: bool = True
    """Render to screen"""


def main(args: Args):
    device = torch.device("cuda" if args.cuda and torch.cuda.is_available() else "cpu")
    env = make_env(args.env, render=args.render)
    action_n = env.unwrapped.action_space.n
    # For atari breakout, we have 4 actions: 0, 1, 2, 3, which are: NOOP, FIRE, LEFT, RIGHT
    print(env.unwrapped.action_space,flush=True)

    agent = Agent(action_n).to(device)
    state_dict = torch.load(args.weights, map_location=device)
    agent.load_state_dict(state_dict)
    agent.eval()

    images = []
    observations = []

    for ep in range(args.episodes):
        obs, _ = env.reset(seed=ep + 42)
        obs = torch.tensor(obs, dtype=torch.float32, device=device).unsqueeze(0)
        observations += [obs]
        done = False
        episodic_return = 0.0
        step = 0
        while not done:
            with torch.no_grad():
                action = agent.act(obs).item()
            obs_np, reward, terminated, truncated, _ = env.step(action)
            episodic_return += float(reward)
            obs = torch.tensor(obs_np, dtype=torch.float32, device=device).unsqueeze(0)
            step += 1
            images += [obs_np[0, :, :]]
            done = bool(terminated or truncated)
        print(f"Episode {ep+1}: return={episodic_return:.2f}")

    env.close()
    np.save("obs.npy", observations[0].cpu().numpy())
    np.save("np_obs.npy", images[0])

    """
    fig, ax = plt.subplots()
    img = ax.imshow(images[0], cmap="gray")
    ax.set_title("Frame 0")

    current = [0]

    def on_key(event):
        if event.key == "right":
            current[0] = (current[0] + 1) % len(images)
        elif event.key == "left":
            current[0] = (current[0] - 1) % len(images)
        else:
            return
        img.set_data(images[current[0]])
        ax.set_title(f"Frame {current[0]}")
        fig.canvas.draw()

    fig.canvas.mpl_connect("key_press_event", on_key)
    plt.show()
    """



if __name__ == "__main__":
    main(tyro.cli(Args))

