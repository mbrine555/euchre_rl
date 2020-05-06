import numpy as np
from rlcard.envs.env import Env

from euchre_trick.game import EuchreGame as Game
from euchre_trick.utils.utils import (ACTION_LIST, ACTION_SPACE, CARD_IDX,
                                      TRUMP_IDX)


class EuchreEnv(Env):

    def __init__(self, config):
        self.game = Game()
        super().__init__(config)
        self.state_shape = [len(CARD_IDX)*2+4]

    def _extract_state(self, state):
        state['legal_actions'] = self._get_legal_actions()
        state['raw_legal_actions'] = self.game.get_legal_actions()
        # State is card indices + last element is trump
        hand = [CARD_IDX[card] for card in state['hand']]
        state_rep = np.zeros(self.state_shape)
        state_rep[hand] = 1
        if len(state['center']) != 0:
            center = [CARD_IDX[card]+len(CARD_IDX) for card in state['center'].values()]
            state_rep[center] = 1
        if state['trump'] is not None:
            state_rep[len(CARD_IDX)*2+TRUMP_IDX[state['trump']]] = 1
        state['obs'] = state_rep
        return state

    def _decode_action(self, action_id):
        return ACTION_LIST[action_id]

    def _get_legal_actions(self):
        legal_actions = self.game.get_legal_actions()
        legal_ids = [ACTION_SPACE[action] for action in legal_actions]
        return legal_ids

    def get_payoffs(self):
        return self.game.get_payoffs()
