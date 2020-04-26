import random
from copy import deepcopy

from euchre_trick.dealer import EuchreDealer as Dealer
from euchre_trick.player import EuchrePlayer as Player
from euchre_trick.judger import EuchreJudger as Judge
from euchre_trick.utils.utils import cards2list

class EuchreGame(object):

    def __init__(self, allow_step_back=False):
        self.allow_step_back = allow_step_back
        self.num_players = 4
        self.payoffs = [0 for _ in range(self.num_players)]

    def init_game(self):
        self.payoffs = [0 for _ in range(self.num_players)]

        self.judge = Judge()

        self.dealer = Dealer()
        self.dealer_player_id = random.randrange(0, self.num_players)
        self.players = [Player(i) for i in range(self.num_players)]

        for player in self.players:
            self.dealer.deal_cards(player, 5)

        self.flipped_card = self.dealer.flip_top_card()
        self.history = []
        self.center = {}
        self.score = {i:0 for i in range(self.num_players)}
        self.trump = None

        self.current_player = self._increment_player(self.dealer_player_id)
        state = self.get_state(self.current_player)
        return state, self.current_player

    def get_state(self, player_id):
        state = {}
        player = self.players[player_id]
        state['hand'] = cards2list(player.hand)
        state['trump_called'] = self.trump is not None
        state['trump'] = self.trump
        if self.flipped_card is not None:
            state['flipped'] = self.flipped_card.get_index()
        else:
            state['flipped'] = None
        state['center'] = {k:v.get_index() for k, v in self.center.items()}
        return state

    def step(self, action):
        if action == 'pick':
            self._perform_pick_action()
            state = self.get_state(self.current_player)
            return state, self.current_player
    
        if action == 'pass':
            self._perform_pass()
            state = self.get_state(self.current_player)
            return state, self.current_player

        if action.startswith('call'):
            suit = action.split('-')[1]
            self._perform_call(suit)
            state = self.get_state(self.current_player)
            return state, self.current_player

        if action.startswith('discard'):
            card = action.split('-')[1]
            self._perform_discard(card)
            state = self.get_state(self.current_player)
            return state, self.current_player
    
        self._play_card(action)
        if len(self.center) == 4:
            self._end_trick()
        state = self.get_state(self.current_player)
        return state, self.current_player

    def _perform_pick_action(self):
        dealer_player = self.players[self.dealer_player_id]
        dealer_player.hand.append(self.flipped_card)
        self.trump = self.flipped_card.suit
        self.flipped_card = None
        self.calling_player = self.current_player
        self.current_player = self.dealer_player_id

    def _increment_player(self, player_id):
        return (player_id+ 1) % self.num_players

    def _perform_discard(self, card):
        player = self.players[self.current_player]
        for index, hand_card in enumerate(player.hand):
            if hand_card.get_index() == card:
                remove_index = index
                break
        card = player.hand.pop(remove_index)
        self.current_player = self._increment_player(self.current_player)

    def _play_card(self, action):
        player = self.players[self.current_player]
        for index, hand_card in enumerate(player.hand):
            if hand_card.get_index() == action:
                remove_index = index
                break
        card = player.hand.pop(remove_index)
        self.center[self.current_player] = card
        self.current_player = self._increment_player(self.current_player)

    def _end_trick(self):
        winner = self.judge.judge_trick(self)
        self.score[winner] += 1
        self.current_player = winner
        self.center = {}

    def _perform_call(self, suit):
        self.trump = suit
        self.current_player = self._increment_player(self.dealer_player_id)

    def _perform_pass(self):
        if self.current_player == self.dealer_player_id:
            self.flipped_card = None
        self.current_player = self._increment_player(self.current_player)
