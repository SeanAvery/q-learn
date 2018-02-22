import gym

env = gym.make('CartPole-v0')

observation = env.reset()

print(env.action_space)

for _ in range(10):
    env.render()
    action = env.action_space.sample()
    print(action)
    env.step(action)
    observation, reward, done, info = env.step(action)
    print(observation)
    input("Press Enter to continue...")
    if done:
        print('episode finished after {} steps'.format(_+1))
        break

