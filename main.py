import argparse
import logging
import os
import importlib

import numpy as np
import gym

from protopost import ProtoPost
from nd_to_json import nd_to_json, json_to_nd

PORT = int(os.getenv("PORT", 80))
ENV_NAME = os.getenv("ENV_NAME", "LunarLanderContinuous-v2")
#reward to give on episode end (since we can't detect DONEs)
EPISODE_REWARD = float(os.getenv("EPISODE_REWARD", 0))

#create env
#import
if ENV_NAME.find(" ") != -1:
  ENV_NAME = ENV_NAME.split(" ")
  env = getattr(importlib.import_module(ENV_NAME[0]), ENV_NAME[1])
  env = env()
else:
  env = gym.make(ENV_NAME)
print(env)

obs = env.reset()

is_discrete = isinstance(env.action_space, gym.spaces.Discrete)

print("Observation space:", env.observation_space)
print("Action space:", env.action_space)

def step(data):
  global obs
  #get action
  action = json_to_nd(data)
  if is_discrete:
    action = int(action)

  #step environment
  obs, reward, done, info = env.step(action)
  done = bool(done)
  reward = float(reward)
  if done:
    obs = env.reset()
    reward += EPISODE_REWARD

  #TODO: fix info (recursively check that each value is json serializable)
  return {"obs":nd_to_json(obs), "done":done, "reward":reward, "info":{}}

def get_observation(data):
  return nd_to_json(obs)

routes = {
  "": step,
  "obs": get_observation
}

ProtoPost(routes).start(PORT)
