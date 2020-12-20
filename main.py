import argparse
import logging
from datetime import datetime
import os

import numpy as np
import gym

from protopost import ProtoPost
from protopost import protopost_client as ppcl

from nd_to_json import nd_to_json, json_to_nd

import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

REWARD_URL = os.getenv("REWARD_URL")
EPISODE_REWARD_URL = os.getenv("EPISODE_REWARD_URL", None)
ACTION_URL = os.getenv("ACTION_URL")
PORT = os.getenv("PORT", 80)
ENV_NAME = os.getenv("ENV_NAME")

observation = None

#create env
env = gym.make(ENV_NAME)
observation = env.reset()
episode_reward = 0

is_discrete = isinstance(env.action_space, gym.spaces.Discrete)

print("Observation space:", env.observation_space)
print("Action space:", env.action_space)

def step(data):
    global observation, episode_reward
    #get action
    action = json_to_nd(ppcl(ACTION_URL))
    if is_discrete:
        action = int(action)

    #step environment
    obs, reward, done, info = env.step(action)
    episode_reward += reward
    if done:
        obs = env.reset()
        if EPISODE_REWARD_URL is not None:
            ppcl(EPISODE_REWARD_URL, episode_reward)
        episode_reward = 0
    observation = obs

    #send reward
    #ppcl(REWARD_URL, nd_to_json(reward))
    ppcl(REWARD_URL, reward)

def get_observation(data):
    return nd_to_json(observation)

routes = {
    "step": step,
    "observation": get_observation
}

ProtoPost(routes).start(PORT)
