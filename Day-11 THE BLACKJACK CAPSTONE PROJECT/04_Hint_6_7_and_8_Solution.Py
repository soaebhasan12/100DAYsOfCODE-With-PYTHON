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




#Hint 6: Create a function called calculate_score() that takes a List of cards as input and returns the score. 
#Look up the sum() function to help you do this.

def calculate_score(cards):
    #Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
    
    #if 11 in cards and 10 in cards and len(cards) == 2:
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    # #Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        return sum(cards)

    return sum(cards)