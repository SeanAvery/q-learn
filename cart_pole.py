import gym
env = gym.make('CartPole-v0')

for i in range(10):
    observation = env.reset()
    for t in range(100):
        env.render()
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print('episode finished after {} timesteps'.format(t+1))
            break
    env.render()
    env.step(env.action_space.sample())

