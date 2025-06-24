#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
import random

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

user_cards = []
computer_cards = []

for _ in range(2):
#    new_card = deal_card()
#   user_cards += new_card
# Above line is same as, but new card should be list type:
#   user_cards.extend(new_card)

#   new_card = [deal_card()]
#   user_cards.extend(new_card)

#   user_cards.append(new_card)

    user_cards.append(deal_card())
    computer_cards.append(deal_card())