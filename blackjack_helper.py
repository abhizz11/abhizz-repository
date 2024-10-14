from random import randint


def print_card_name(card_rank):
    if card_rank == 1:
        print('Drew an Ace')
    elif card_rank <= 10 and card_rank > 1 and card_rank != 8:
        print(f'Drew a {card_rank}')
    elif card_rank == 8:
        print(f'Drew an {card_rank}')
    elif card_rank == 11:
        print(f'Drew a Jack')
    elif card_rank == 12:
        print(f'Drew a Queen')
    elif card_rank == 13:
        print(f'Drew a King')
    else:
        print('BAD CARD')


def draw_card():
    card_value = randint(1, 13)
    if card_value == 1:
        print_card_name(card_value)
        return 11
    elif card_value == 8:
        print_card_name(card_value)
        return 8
    elif card_value <= 10 and (card_value != 1 or card_value != 8):
        print_card_name(card_value)
        return card_value
    elif card_value == 11:
        print_card_name(card_value)
        return 10
    elif card_value == 12:
        print_card_name(card_value)
        return 10
    elif card_value == 13:
        print_card_name(card_value)
        return 10


def print_header(message):
    print('-----------')
    print(f'{message}')
    print('-----------')


def draw_starting_hand(name):
    print_header(f'{name} TURN')
    card_1 = draw_card()
    card_2 = draw_card()
    total = card_1 + card_2
    return total


def print_end_turn_status(hand_value):
    if hand_value > 21:
        print(f'Final hand: {hand_value}.')
        print("BUST.")
    elif hand_value == 21:
        print(f'Final hand: {hand_value}.')
        print('BLACKJACK!')
    else:
        print(f'Final hand: {hand_value}.')


def print_end_game_status(user_hand, dealer_hand):
    print_header('GAME RESULT')
    if user_hand > 21 and dealer_hand > 21:
        print("Dealer wins!")
    elif user_hand == dealer_hand:
        print("Push.")
    elif dealer_hand == 21:
        print("Dealer wins!")
    elif user_hand > 21:
        print("Dealer wins!")
    elif user_hand < 21 and dealer_hand < 21 and user_hand < dealer_hand:
        print("Dealer wins!")
    elif user_hand == 21:
        print("You win!")
    elif dealer_hand > 21:
        print("You win!")
    elif user_hand < 21 and dealer_hand < 21 and user_hand > dealer_hand:
        print("You win!")
