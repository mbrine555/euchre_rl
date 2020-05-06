from collections import defaultdict

import numpy as np

from euchre_trick.utils.utils import LEFT, NON_TRUMP

class EuchreRuleAgent(object):

    def __init__(self):
        self.use_raw = True

    def step(self, state):
        legal_actions = state['raw_legal_actions']
        hand = state['hand']

        #if len(legal_actions) == 1:
        #    return legal_actions[0]

        if len(hand) == 6:
            suit_counts = self.count_suits(hand, include_left=False)
            worst_suit = min(suit_counts, key = suit_counts.get)
            cards = [card for card in hand if card[0] == worst_suit]
            worst_card = [NON_TRUMP.index(card[1]) for card in cards]
            discard = cards[np.argmin(worst_card)]
            return f'discard-{discard}'

        if not state['trump_called']:
            suit_counts = self.count_suits(hand)
            best_suit = max(suit_counts, key = suit_counts.get)  
            if state['flipped'] is not None:
                if suit_counts[state['flipped'][0]] >= 3:
                    return 'pick'
                return 'pass'
            else:
                if suit_counts[best_suit] >= 3 and best_suit != state['turned_down']:
                    return f"call-{best_suit}"
                if 'pass' not in legal_actions:
                    return np.random.choice(legal_actions)
                return 'pass'
        
        has_right = (state['trump'] + 'J') in legal_actions
        if has_right and len(state['center']) == 0:
            return state['trump'] + 'J'

        playable_trump = [card for card in legal_actions if card[0] == state['trump']]
        if len(playable_trump) > 0:
            worst_card = [NON_TRUMP.index(card[1]) for card in playable_trump]
            return playable_trump[np.argmin(worst_card)]

        aces = [card for card in legal_actions if card[0] != state['trump'] and card[1] == 'A']
        if len(aces) > 0:
            return aces[0]
        
        worst_card = [NON_TRUMP.index(card[1]) for card in legal_actions]
        if len(worst_card) > 0:
            return legal_actions[np.argmin(worst_card)]
            
        return np.random.choice(legal_actions)        


    def eval_step(self, state):
        return self.step(state), []

    @staticmethod
    def count_suits(hand, include_left=True):
        card_count = defaultdict(int)
        for card in hand:
            card_count[card[0]] += 1
            if include_left:
                if card[1] == 'J':
                    card_count[LEFT[card[0]][0]] += 1
        return card_count