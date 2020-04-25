non_trump = ['9', 'T', 'J', 'Q', 'K', 'A']
left = {'D': 'HJ', 'H': 'DJ', 'C':'SJ', 'S':'CJ'}

class EuchreJudger(object):
    
    def __init__(self):
        pass

    def judge_trick(self, game):
        center_cards = game.center
        trump = game.trump
        leader = game.current_player
        player_order = self._get_player_order(leader)
        
        lead_suit = center_cards[leader].suit
        winning_card = center_cards[leader]
        
        if self._is_right(winning_card, trump):
            return [k for k, v in center_cards.items() if winning_card == v][0]

        for player in player_order[1:]:
            candidate_card = center_cards[player]
            
            if self._is_right(candidate_card, trump):
                winning_card = candidate_card
                break

            if self._is_left(winning_card, trump):
                continue

            if self._is_left(candidate_card, trump):
                winning_card = candidate_card
                continue

            if (candidate_card.suit != trump):
                if candidate_card.suit == lead_suit:
                    if non_trump.index(candidate_card.rank) > non_trump.index(winning_card.rank):
                        winning_card = candidate_card
                        continue
            
            if (candidate_card.suit == trump):
                if candidate_card.suit != winning_card.suit:
                    winning_card = candidate_card
                    continue
                if non_trump.index(candidate_card.rank) > non_trump.index(winning_card.rank):
                    winning_card = candidate_card
                    continue
        
        return [k for k, v in center_cards.items() if winning_card == v][0]

    def _get_player_order(self, leader):
        return [(i+leader)%4 for i in range(4)]

    def _is_left(self, card, trump):
        return card.get_index() == left[trump]

    def _is_right(self, card, trump):
        return card.get_index() == trump + 'J'