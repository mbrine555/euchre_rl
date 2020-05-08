from rlcard.agents.random_agent import RandomAgent
from rlcard.agents.dqn_agent_pytorch import DQNAgent
from rlcard.utils.logger import Logger
from rlcard.utils.utils import tournament

from euchre_trick.agents.rule_agent import EuchreRuleAgent
from euchre_trick.env import EuchreEnv

DEFAULT_CONFIG = {
    'allow_step_back': False,
    'allow_raw_data': False,
    'single_agent_mode' : False,
    'active_player' : 0,
    'record_action' : False,
}

env = EuchreEnv(DEFAULT_CONFIG)
eval_env = EuchreEnv(DEFAULT_CONFIG)

# All random = 0.00411
# Rule Agent Alone = 0.09185
# Rule Agent Team = 0.19251
# Bid Rule = 0.0438

agent = DQNAgent(scope='dqn', 
                 action_num=env.action_num,
                 state_shape=env.state_shape,
                 batch_size=64,
                 mlp_layers=[64])

env.set_agents([agent, 
                RandomAgent(action_num=env.action_num), 
                RandomAgent(action_num=env.action_num), 
                RandomAgent(action_num=env.action_num)])

eval_env.set_agents([agent, 
                     RandomAgent(action_num=env.action_num), 
                     RandomAgent(action_num=env.action_num), 
                     RandomAgent(action_num=env.action_num)])

logger = Logger('.')
for episode in range(100000):
    # Generate data from the environment
    trajectories, _ = env.run(is_training=True)
    # Feed transitions into agent memory, and train the agent
    for ts in trajectories[0]:
        agent.feed(ts)
    # Evaluate the performance. Play with random agents.
    if episode % 5000 == 0:
        logger.log_performance(env.timestep, tournament(eval_env, 10000)[0])

logger.close_files()
logger.plot('DQN')