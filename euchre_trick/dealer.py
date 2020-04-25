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

    def deal_cards(self, player, num):
        for _ in range(num):
            card = self.deck.pop()
            player.hand.append(card)

    def flip_top_card(self):
        top_card = self.deck.pop()
        return top_card