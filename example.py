from rlcard.agents.random_agent import RandomAgent
from rlcard.utils.utils import tournament

from euchre_trick.env import EuchreEnv
from euchre_trick.agents.rule_agent import EuchreRuleAgent

DEFAULT_CONFIG = {
    'allow_step_back': False,
    'allow_raw_data': False,
    'single_agent_mode' : False,
    'active_player' : 0,
    'record_action' : False,
}

env = EuchreEnv(DEFAULT_CONFIG)
# All random = 0.00411
# Calling rules = 0.07179
# Discard rules = 0.09611
# Always lead right = 0.10881
# Play worst trump = 0.16114
# Play off Ace = 0.18589
# Play worst card = 0.19251
env.set_agents([RandomAgent(action_num=env.action_num), 
                EuchreRuleAgent(), 
                RandomAgent(action_num=env.action_num), 
                EuchreRuleAgent()])

tournament(env, 100000)
