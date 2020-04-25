import random

from euchre_trick.utils.utils import init_euchre_deck


class EuchreDealer(object):

    def __init__(self):
        super().__init__()
        self.deck = init_euchre_deck()
        self.shuffle()
        self.hand = []

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self, player):
        card = self.deck.pop()
        player.hand.append(card)