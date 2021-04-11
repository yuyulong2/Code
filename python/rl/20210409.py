# -*-coding:utf-8-*-

import gym
env = gym.make('Taxi-v2')
observation = env.reset()
agent = env.load_agent()
for step in range(100):
    action = agent(observation)
    observation,reward,done,info = env.step(action)