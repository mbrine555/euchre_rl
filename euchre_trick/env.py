from rlcard.envs.env import Env
from euchre_trick.game import EuchreGame as Game

class EuchreEnv(Env):

    def __init__(self, config):
        self.game = Game()
        super().__init__(config)
        