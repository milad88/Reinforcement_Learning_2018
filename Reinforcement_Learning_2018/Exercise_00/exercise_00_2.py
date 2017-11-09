import gym
env = gym.make('CartPole-v0')
global done
done = False
for i_episode in range(20):

    observation = env.reset()

    for t in range(100):

        env.render()

        def try_func(n):
            for i in range(n):
                action = env.action_space.sample()
                observation, reward, done, info = env.step(action)
                print(observation)

        try_func(20)
        if done:

            observation = env.reset()
            try_func(10)
            if done:
                print("Episode finished after {} timesteps".format(t+1))
                break
