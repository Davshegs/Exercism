"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """
    rounds = [number, number + 1, number + 2]
    return rounds 
    
print(get_rounds(27))


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
    new_rounds = rounds_1 + rounds_2
    return new_rounds

print(concatenate_rounds([27, 28, 29], [35, 36]))

def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """
    return bool(number in rounds)

print(list_contains_round([27, 28, 29, 35, 36], 29))
print(list_contains_round([27, 28, 29, 35, 36], 30))


def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """
    card_avg = (sum(hand) / len(hand))
    return card_avg

print(card_average([5, 6, 7]))

def approx_average_is_average(hand):
    """Return if an average is using (first + last index values ) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """
    main_avg = (sum(hand) / len(hand))
    first_and_last_avg = (hand[0] + hand[-1]) / 2
    median = hand[len(hand)// 2]
    return bool(main_avg in (first_and_last_avg , median))

print(approx_average_is_average([1, 2, 3]))
print(approx_average_is_average([2, 3, 4, 8, 8]))
print(approx_average_is_average([1, 2, 3, 5, 9]))

def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    even_card = hand[::2]
    odd_card = hand[1::2]
    average_even_card = sum(even_card) / len(even_card)
    average_odd_card = sum(odd_card) / len(odd_card)
    return bool(average_even_card == average_odd_card)

print(average_even_is_average_odd([1, 2, 3]))
print(average_even_is_average_odd([1, 2, 3, 4]))

def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    if hand[-1] == 11:
        hand[-1] = hand[-1] * 2
        return hand
    return hand

print(maybe_double_last([5, 9, 11]))
print(maybe_double_last([5, 9, 10]))