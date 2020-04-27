from rlcard.envs.env import Env
from euchre_trick.game import EuchreGame as Game
from euchre_trick.utils.utils import ACTION_SPACE, ACTION_LIST

class EuchreEnv(Env):

    def __init__(self, config):
        self.game = Game()
        super().__init__(config)

    def _extract_state(self, state):
        state['legal_actions'] = self._get_legal_actions()
        return state

    def _decode_action(self, action_id):
        return ACTION_LIST[action_id]

    def _get_legal_actions(self):
        legal_actions = self.game.get_legal_actions()
        legal_ids = [ACTION_SPACE[action] for action in legal_actions]
        return legal_ids

    def get_payoffs(self):
        return self.game.get_payoffs()