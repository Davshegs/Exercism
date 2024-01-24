""" Function to help play and score a game of black Jack """

face_cards = ['J', 'Q', 'K']

def value_of_card(card):
    """ Determing the scoring value of a card
    
    :param card: str - given card
    :return int: value of the given card. See below for the values

    1. 'J', 'K', 'Q' (otherwise known as the "face cards") = 10
    2. 'A' (ace) = 1
    3. '2' - '10' = numerical value.

    """
    if card in face_cards:
        return 10
    if card == 'A':
        return 1
    return int(card)

print(value_of_card('K'))
print(value_of_card('4'))
print(value_of_card('A'))


def higher_card(card_one, card_two):
    """ Determining which card has the highest value

    :param card_one , card_two: str - cards dealt in hand. See below for values.
    :return: str or tuple - resulting tuples arise if both card are of the same value.

    1. 'J', 'K', 'Q' (otherwise known as the "face cards") = 10
    2. 'A' (ace) = 1
    3. '2' - '10' = numerical value.

    """
    if value_of_card(card_one) == value_of_card(card_two):
        return card_one , card_two
    if value_of_card(card_one) > value_of_card(card_two):
        return card_one
    return card_two

print(higher_card('K', '10'))
print(higher_card('4', '6'))
print(higher_card('K', 'A'))

def value_of_ace(card_one, card_two):
    """ Calculating the most advantageous value of the ace card

    ;param card_one, card_two: str - cards dealt. See below for values.
    :return int: returning 1 or 11 for the upcoming ace card.

    1. 'J', 'K', 'Q' (otherwise known as the "face cards") = 10
    2. 'A' (ace) = 11 (if already at hand)
    3. '2' - '10' = numerical value.

    """
    def value_of_card2(card):
        if card in face_cards:
            return 10
        if card == 'A':
            return 11
        return int(card)
    sum_of_cards = value_of_card2(card_one) + value_of_card2(card_two)
    if (sum_of_cards + 11) > 21:
        return 1
    return 11

print(value_of_ace('6', 'K'))
print(value_of_ace('7', 'A'))

def is_blackjack(card_one, card_two):
    """ Determing if the hand is a 'natural' or a 'blackjack'. 

    :param card_one, card_two: str - cards dealt. See below for values.
    :return bool - is the hand is a blackjack (two card worth 21)

    1. 'J', 'K', 'Q' (otherwise known as the "face cards") = 10
    2. 'A' (ace) = 11 (if already at hand)
    3. '2' - '10' = numerical value.

    """
    ten_card = [10, 'K', 'Q', 'J']
    def value_of_card2(card):
        if card in ten_card:
            return 10
        if card == 'A':
            return 11
        return int(card)
    return bool((value_of_card2(card_one) + value_of_card2(card_two)) == 21 )

print(is_blackjack('A', 'K'))
print(is_blackjack('10', '9'))

def can_split_pairs(card_one, card_two):
    """ Determine if a player can split their hands into two hands

    :param card_one , card_two: str - card dealt.
    :return bool - can the hand be split into two pairs?(i.e cards are of the same values)

    """
    def value_of_card2(card):
        if card in face_cards:
            return 10
        if card == 'A':
            return 11
        return int(card)
    return bool(value_of_card(card_one) == value_of_card(card_two))

print(can_split_pairs('Q', 'K'))
print(can_split_pairs('10', 'A'))

def can_double_down(card_one, card_two):
    """Determine if the blackjack player can place a double down bet
    
    :param card_one, card_two: str - frist and second card in hand
    :return bool - can the hnad can be double down? (i.e totals 9, 10 or 11 points)
    
    """
    total_point = [9, 10, 11] 
    return bool((value_of_card(card_one) + value_of_card(card_two)) in total_point)

print(can_double_down('A', '9'))
print(can_double_down('10', '2'))
