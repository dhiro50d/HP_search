# CartPole-v1
# https://www.gymlibrary.dev/environments/classic_control/cart_pole/
# REINFORCE algorizm

import gym
import torch
import torch.nn as nn
import torch.optim as optim


class PolicyNetwork(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(PolicyNetwork, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return torch.softmax(x, dim=0)


def train(agent, episodes, env):
    optimizer = optim.Adam(agent.parameters(), lr=0.001)
    criterion = nn.CrossEntropyLoss()

    for episode in range(episodes):
        state = env.reset()
        done = False
        episode_reward = 0
        state = state[0]  # state: Tumple[List[float], Dict]
        while not done:
            state = torch.tensor(state, dtype=torch.float32)
            action_probs = agent(state)
            action = torch.multinomial(action_probs, 1).item()

            next_state, reward, done, _, _ = env.step(action)
            episode_reward += reward
            reward = -10 if done else 1
            next_state = torch.tensor(next_state, dtype=torch.float32)

            optimizer.zero_grad()
            pred = agent(state.unsqueeze(0))
            target = torch.tensor([action])
            loss = criterion(pred, target)
            loss.backward()
            optimizer.step()

            state = next_state
            torch.save(agent.state_dict(), 'cartpole_model.pth')

        if episode % 10 == 0:
            print(f"Episode {episode}, Reward: {episode_reward}")


if __name__ == "__main__":
    env = gym.make('CartPole-v1')
    input_size = env.observation_space.shape[0]
    hidden_size = 128
    output_size = env.action_space.n

    agent = PolicyNetwork(input_size, hidden_size, output_size)
    train(agent, episodes=200, env=env)
    print("train finishe.")

    agent.load_state_dict(torch.load('cartpole_model.pth'))
    agent(torch.tensor(env.reset()[0]))
    print("valid finishe")
