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
is_game_over = False

#Hint 6: Create a function called calculate_score() that takes a List of cards as input and returns the score. 
#Look up the sum() function to help you do this.

def calculate_score(cards):
    """take a list of cards and return the score calcilated from the cards"""
    
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

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())



#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

while not is_game_over:
    
    #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    computer_score = calculate_score(computer_cards)
    user_score = calculate_score(user_cards)

    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
        user_should_deal = input("Type 'y' to get another card, type 'n' to pass:  ")    
        if user_should_deal == 'y':
            user_cards.append(deal_card())
        else:
            is_game_over = True        
    
    
    
    
#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer = calculate_score(computer_cards)