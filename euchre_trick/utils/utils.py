from rlcard.core import Card, Player

LEFT = {'D': 'HJ', 'H': 'DJ', 'C':'SJ', 'S':'CJ'}

ACTION_SPACE = {
    'pass': 0,
    'pick': 1,
    'call-H': 2,
    'call-D': 3,
    'call-S': 4,
    'call-C': 5,
    'HA': 6,
    'HK': 7,
    'HQ': 8,
    'HJ': 9,
    'HT': 10,
    'H9': 11,
    'DA': 12,
    'DK': 13,
    'DQ': 14,
    'DJ': 15,
    'DT': 16,
    'D9': 17,
    'SA': 18,
    'SK': 19,
    'SQ': 20,
    'SJ': 21,
    'ST': 22,
    'S9': 23,
    'CA': 24,
    'CK': 25,
    'CQ': 26,
    'CJ': 27,
    'CT': 28,
    'C9': 29,
    'discard-HA': 30,
    'discard-HK': 31,
    'discard-HQ': 32,
    'discard-HJ': 33,
    'discard-HT': 34,
    'discard-H9': 35,
    'discard-DA': 36,
    'discard-DK': 37,
    'discard-DQ': 38,
    'discard-DJ': 39,
    'discard-DT': 40,
    'discard-D9': 41,
    'discard-SA': 42,
    'discard-SK': 43,
    'discard-SQ': 44,
    'discard-SJ': 45,
    'discard-ST': 46,
    'discard-S9': 47,
    'discard-CA': 48,
    'discard-CK': 49,
    'discard-CQ': 50,
    'discard-CJ': 51,
    'discard-CT': 52,
    'discard-C9': 53
}

ACTION_LIST = list(ACTION_SPACE.keys())

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