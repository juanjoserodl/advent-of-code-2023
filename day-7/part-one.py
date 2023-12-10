with open('day-7/input/input.txt''', 'r') as file:
    data = [line.strip() for line in file.readlines()]

hands_bids = [line.split() for line in data]
hands = [hand_bid[0] for hand_bid in hands_bids]

CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

def get_hand_type(hand):
    '''
    7: five of a kind   AAAAA   1 unique cards
    6: four of a kind   AA8AA   2
    5: full house       23332   2
    4: three of a kind  TTT98   3
    3: two pair         23432   3
    2: one pair         A23A4   4
    1: high card        23456   5 
    '''
    num_unique_cards = len(set(hand))
    max_per_card_count = max([hand.count(card) for card in set(hand)])

    if num_unique_cards == 1:
        return 7
    if num_unique_cards == 2 and max_per_card_count == 4:
        return 6
    if num_unique_cards == 2 and max_per_card_count == 3:
        return 5
    if num_unique_cards == 3 and max_per_card_count == 3:
        return 4
    if num_unique_cards == 3 and max_per_card_count == 2:
        return 3
    if num_unique_cards == 4:
        return 2
    if num_unique_cards == 5:
        return 1


def calculate_second_order_value(hand):
    '''
    Will be calculated based on the following formula:

        The sum of: card_value * 10**(card_length * 2 - card_position * 2) for each card in hand

        card_value: card index in reversed CARDS list
        card_lenght: fixed value, 5 (multiplied by 2, to avoid issues with cards with value greater than 10) 
        card_position: card index in hand 

    Example:  34567
        - 1 * 10**(10-0*2) = 10000000000    
        - 2 * 10**(10-1*2) =   200000000
        - 3 * 10**(10-2*2) =     3000000
        - 4 * 10**(10-3*2) =       40000
        - 5 * 10**(10-4*2) =         500
                    sum    = 10203040500
    '''
    second_order_values = [CARDS.index(card) * 10**(10-pos*2) for pos, card in enumerate(hand)]
    return sum(second_order_values)

hands_type = [(hand, get_hand_type(hand), calculate_second_order_value(hand)) for hand in hands]
hands_sorted = sorted(hands_type, key=lambda x: (x[1], x[2]), reverse=True)
total_winnings = [int(hands_bids[hands.index(hand[0])][1]) * (len(hands_sorted)-i) for i, hand in enumerate(hands_sorted)] 

print(sum(total_winnings)) # 248450290
