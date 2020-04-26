from rlcard.core import Card, Player

LEFT = {'D': 'HJ', 'H': 'DJ', 'C':'SJ', 'S':'CJ'}

def init_euchre_deck():
    ''' Initialize a standard deck of 52 cards
    Returns:
        (list): A list of Card object
    '''
    suit_list = ['S', 'H', 'D', 'C']
    rank_list = ['A', '9', 'T', 'J', 'Q', 'K']
    res = [Card(suit, rank) for suit in suit_list for rank in rank_list]
    return res

def cards2list(cards):
    return [card.get_index() for card in cards]

def is_left(card, trump):
    return card.get_index() == LEFT[trump]

def is_right(card, trump):
    return card.get_index() == trump + 'J'