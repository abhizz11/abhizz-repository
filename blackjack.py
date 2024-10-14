
from blackjack_helper import *

user_hand_value = draw_starting_hand('YOUR')
is_yes = True
new_card = 0
while user_hand_value < 21 and is_yes:
    should_hit = input(f'You have {user_hand_value}. Hit (y/n)? ')
    if should_hit == 'n':
        is_yes = False
    elif should_hit == 'y':
        new_card = draw_card()
        user_hand_value = user_hand_value + new_card
    else:
        print("Sorry I didn't get that.")
print_end_turn_status(user_hand_value)

dealer_hand_value = draw_starting_hand('DEALER')
dealer_new_card = 0
while dealer_hand_value < 17:
    print(f"Dealer has {dealer_hand_value}.")
    dealer_new_card = draw_card()
    dealer_hand_value = dealer_hand_value + dealer_new_card

print_end_turn_status(dealer_hand_value)
print_end_game_status(user_hand_value, dealer_hand_value)
