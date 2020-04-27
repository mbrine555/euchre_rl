from euchre_trick.env import EuchreEnv
from rlcard.agents.random_agent import RandomAgent

DEFAULT_CONFIG = {
    'allow_step_back': False,
    'allow_raw_data': False,
    'single_agent_mode' : False,
    'active_player' : 0,
    'record_action' : False,
}

env = EuchreEnv(DEFAULT_CONFIG)
env.set_agents([RandomAgent(action_num=env.action_num), 
                RandomAgent(action_num=env.action_num), 
                RandomAgent(action_num=env.action_num), 
                RandomAgent(action_num=env.action_num)])

trajectories, _ = env.run(is_training=False)
