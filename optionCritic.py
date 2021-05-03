from collector import Collector
import torch
import torch.nn as nn
from torch.distributions import Categorical, Bernoulli

from math import exp
import numpy as np

from save import Save
from game import Game
from auxillaries import loop
from helper import device
from copy import deepcopy
from replaybuffer import ReplayBuffer


class OptionCriticConv(nn.Module):
    def __init__(self,
                 in_features,
                 num_actions,
                 num_options,
                 width,
                 height,
                 temperature=1.0,
                 eps_start=1.0,
                 eps_min=0.1,
                 eps_decay=int(1e6),
                 eps_test=0.05,
                 device='cpu',
                 testing=False):

        super(OptionCriticConv, self).__init__()

        self.in_channels = in_features
        self.num_actions = num_actions
        self.num_options = num_options
        self.magic_number = 7 * 7 * 64
        self.device = device
        self.testing = testing

        self.temperature = temperature
        self.eps_min = eps_min
        self.eps_start = eps_start
        self.eps_decay = eps_decay
        self.eps_test = eps_test
        self.num_steps = 0

        # self.features = nn.Sequential(
        #     nn.Conv2d(self.in_channels, 32, kernel_size=8, stride=4),
        #     nn.ReLU(),
        #     nn.Conv2d(32, 64, kernel_size=4, stride=2),
        #     nn.ReLU(),
        #     nn.Conv2d(64, 64, kernel_size=3, stride=1),
        #     nn.ReLU(),
        #     nn.modules.Flatten(),
        #     nn.Linear(self.magic_number, 512),
        #     nn.ReLU()
        # )

        self.features = nn.Sequential(nn.Conv2d(self.in_channels, 128, 5), nn.LeakyReLU(), nn.Conv2d(128, 64, 3), nn.LeakyReLU(), nn.Flatten(), nn.Linear(64 * (width - 6) * (height - 6), 128), nn.LeakyReLU(), nn.Linear(128, 128), nn.ReLU())  # , nn.Flatten()

        self.Q = nn.Linear(128, num_options)                 # Policy-Over-Options
        self.terminations = nn.Linear(128, num_options)                 # Option-Termination
        self.options_W = nn.Parameter(torch.zeros(num_options, 128, num_actions))
        self.options_b = nn.Parameter(torch.zeros(num_options, num_actions))

        self.to(device)
        self.train(not testing)

    def get_state(self, obs):
        if obs.ndim < 4:
            obs = obs.unsqueeze(0)
        obs = obs.to(self.device)
        state = self.features(obs)
        return state

    def get_Q(self, state):
        return self.Q(state)

    def predict_option_termination(self, state, current_option):
        termination = self.terminations(state)[:, current_option].sigmoid()
        option_termination = Bernoulli(termination).sample()

        Q = self.get_Q(state)
        next_option = Q.argmax(dim=-1)
        return bool(option_termination.item()), next_option.item()

    def get_terminations(self, state):
        return self.terminations(state).sigmoid()

    def get_action(self, state, option):
        logits = state @ self.options_W[option] + self.options_b[option]
        action_dist = (logits / self.K_).softmax(dim=-1)
        action_dist = Categorical(action_dist)

        action = action_dist.sample()
        logp = action_dist.log_prob(action)
        entropy = action_dist.entropy()
        return action.item(), logp, entropy

    def greedy_option(self, state):
        Q = self.get_Q(state)
        return Q.argmax(dim=-1)

    @property
    def epsilon(self):
        self.num_steps += 1
        return max(self.eps_min, 1 - self.num_steps / self.eps_decay)

    @property
    def K_(self):
        return max(self.temperature, self.temperature * (1000000 / self.num_steps))



def critic_loss_fn(model, model_prime, data_batch):
    obs, options, rewards, next_obs, dones = data_batch
    batch_idx = torch.arange(len(options)).long()
    masks = 1 - dones

    # The loss is the TD loss of Q and the update target, so we need to calculate Q
    states = model.get_state(obs).squeeze(0)
    Q = model.get_Q(states)

    # the update target contains Q_next, but for stable learning we use prime network for this
    next_states_prime = model_prime.get_state(next_obs).squeeze(0)
    next_Q_prime = model_prime.get_Q(next_states_prime)  # detach?

    # Additionally, we need the beta probabilities of the next state
    next_states = model.get_state(next_obs).squeeze(0)
    next_termination_probs = model.get_terminations(next_states).detach()
    next_options_term_prob = next_termination_probs[batch_idx, options]

    # Now we can calculate the update target gt
    gt = rewards + masks * 0.95 * \
        ((1 - next_options_term_prob) * next_Q_prime[batch_idx, options] + next_options_term_prob * next_Q_prime.max(dim=-1)[0])

    # to update Q we want to use the actual network, not the prime
    td_err = (Q[batch_idx, options] - gt.detach()).pow(2).mul(0.5).mean()
    return td_err


def actor_loss_fn(obs, option, logp, entropy, reward, done, next_obs, model, model_prime):
    state = model.get_state(obs)
    next_state = model.get_state(next_obs)
    next_state_prime = model_prime.get_state(next_obs)

    option_term_prob = model.get_terminations(state)[:, option]
    next_option_term_prob = model.get_terminations(next_state)[:, option].detach()

    Q = model.get_Q(state).detach().squeeze()
    next_Q_prime = model_prime.get_Q(next_state_prime).detach().squeeze()

    # Target update gt
    gt = reward + (1 - done) * 0.98 * ((1 - next_option_term_prob) * next_Q_prime[option] + next_option_term_prob * next_Q_prime.max(dim=-1)[0])

    # The termination loss
    termination_loss = option_term_prob * (Q[option].detach() - Q.max(dim=-1)[0].detach() + 0.01) * (1 - done)

    # actor-critic policy gradient with entropy regularization
    #print(obs)
    policy_loss = -logp * (gt.detach() - Q[option]) - 0.01 * entropy
    actor_loss = termination_loss + policy_loss
    return actor_loss


# parser.add_argument('--env', default='CartPole-v0', help='ROM to run')
# parser.add_argument('--optimal-eps', type=float, default=0.05, help='Epsilon when playing optimally')
# parser.add_argument('--frame-skip', default=4, type=int, help='Every how many frames to process')
# parser.add_argument('--learning-rate', type=float, default=.0005, help='Learning rate')
# parser.add_argument('--gamma', type=float, default=.99, help='Discount rate')
# parser.add_argument('--epsilon-start',  type=float, default=1.0, help=('Starting value for epsilon.'))
# parser.add_argument('--epsilon-min', type=float, default=.1, help='Minimum epsilon.')
# parser.add_argument('--epsilon-decay', type=float, default=20000, help=('Number of steps to minimum epsilon.'))
# parser.add_argument('--max-history', type=int, default=10000, help=('Maximum number of steps stored in replay'))
# parser.add_argument('--batch-size', type=int, default=32, help='Batch size.')
# parser.add_argument('--freeze-interval', type=int, default=200, help=('Interval between target freezes.'))
# parser.add_argument('--update-frequency', type=int, default=4, help=('Number of actions before each SGD update.'))
# parser.add_argument('--termination-reg', type=float, default=0.01, help=('Regularization to decrease termination prob.'))
# parser.add_argument('--entropy-reg', type=float, default=0.01, help=('Regularization to increase policy entropy.'))
# parser.add_argument('--num-options', type=int, default=2, help=('Number of options to create.'))
# parser.add_argument('--temp', type=float, default=1, help='Action distribution softmax tempurature param.')
# parser.add_argument('--max_steps_ep', type=int, default=18000, help='number of maximum steps per episode.')
# parser.add_argument('--max_steps_total', type=int, default=int(4e6), help='number of maximum steps to take.')  # bout 4 million
# parser.add_argument('--cuda', type=bool, default=True, help='Enable CUDA training (recommended if possible).')
# parser.add_argument('--seed', type=int, default=0, help='Random seed for numpy, torch, random.')
# parser.add_argument('--logdir', type=str, default='runs', help='Directory for logging statistics')
# parser.add_argument('--exp', type=str, default=None, help='optional experiment name')
# parser.add_argument('--switch-goal', type=bool, default=False, help='switch goal after 2k eps')

update_frequency = 10
freeze_interval = 10000


def option_critic_run(defaults):
    collector = Collector(**defaults)
    env = Game(**defaults)
    buffer = ReplayBuffer(**defaults)
    batch = env.batch
    num_options = len(env.layers.layers)-3
    option_critic = OptionCriticConv(
        in_features=env.board.shape[1],
        num_actions=4,
        num_options=num_options,
        width=env.board.shape[2],
        height=env.board.shape[3],
        temperature=0.001,
        eps_start=1000000,
        eps_min=0.01,
        eps_decay=1000000,
        eps_test=0.05,
        device=device
    )
    # Create a prime network for more stable Q values
    option_critic_prime = deepcopy(option_critic)
    optim = torch.optim.RMSprop(option_critic.parameters(), lr=0.0005)

    with Save(env, collector, **defaults) as save:
        states = option_critic.get_state(env.board)
        greedy_options = [e.item() for e in list(option_critic.greedy_option(states))]
        current_options = [0 for _ in range(batch)]
        option_terminations = [True for _ in range(batch)]
        dones = [False for _ in range(batch)]
        actions, logps, entropys = [None for _ in range(batch)], [None for _ in range(batch)], [None for _ in range(batch)]
        for frame in loop(env, collector, save):

            epsilon = option_critic.epsilon
            #print(epsilon)
            states = option_critic.get_state(env.board)
            #print(states.shape)
            for i, done in enumerate(dones):
                if done:
                    greedy_options[i] = option_critic.greedy_option(states[i]).item()
                    current_options[i] = 0
                    option_terminations[i] = True
                    actions[i] = None
                    logps[i] = None
                    entropys[i] = None
            #print(greedy_options)

            for i, (option_termination, current_option, state, greedy_option) in enumerate(zip(option_terminations, current_options, states, greedy_options)):
                if option_termination:
                    current_options[i] = np.random.choice(num_options) if np.random.rand() < epsilon else greedy_option

                actions[i], logps[i], entropys[i] = option_critic.get_action(state, current_option)
            # print(logps[0], entropys[0])
            old_obses = env.board
            next_obses, rewards, dones, _ = env.step(torch.tensor(actions))
            collector.collect([rewards], [dones])
            buffer.save_option_critic(old_obses, current_options, rewards, next_obses, dones)
            states = option_critic.get_state(next_obses)
            loss = 0
            for i, (next_obs, reward, done, state, current_option, old_obs, logp, entropy) in enumerate(zip(next_obses, rewards, dones, states, current_options, old_obses, logps, entropys)):
                option_terminations[i], greedy_options[i] = option_critic.predict_option_termination(state.unsqueeze(0), current_option)
                loss += actor_loss_fn(old_obs, current_option, logp, entropy, reward, done, next_obs, option_critic, option_critic_prime)

            if frame % update_frequency == 0:
                data_batch = buffer.sample_option_critic()
                loss += critic_loss_fn(option_critic, option_critic_prime, data_batch)
            optim.zero_grad()
            loss.backward()
            optim.step()
            if frame % freeze_interval == 0:
                option_critic_prime = deepcopy(option_critic)
