import gymnasium as gym
from gymnasium.utils.play import play
import ale_py                      # ensure ALE envs are registered
import pygame                      # for key codes


from atari_wrappers import (  # isort:skip
    ClipRewardEnv,
    EpisodicLifeEnv,
    FireResetEnv,
    MaxAndSkipEnv,
    NoopResetEnv,
)

# 0=NOOP, 1=FIRE, 2=RIGHT, 3=LEFT
keys_to_action = {
    (pygame.K_SPACE,): 1,          # Space to (re)serve
    (pygame.K_RIGHT,): 2,          # Right arrow
    (pygame.K_LEFT,): 3,           # Left arrow
}

env = gym.make("ALE/Breakout-v5", render_mode="rgb_array", frameskip=1)
env = NoopResetEnv(env, noop_max=30)
env = MaxAndSkipEnv(env, skip=4)
env = EpisodicLifeEnv(env)
env = ClipRewardEnv(env)
env = gym.wrappers.ResizeObservation(env, (84, 84))
env = gym.wrappers.GrayscaleObservation(env)
env = gym.wrappers.FrameStackObservation(env, 4)

play(
    env,
    keys_to_action=keys_to_action,
    fps=60,
    zoom=3,
    noop=0,                        # action when no key is pressed
)

