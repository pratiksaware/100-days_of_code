import random
from art import logo


def deal_card():
    """ Deals the cards to the players"""

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0


    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(u_score,c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "You lose, Computer has a blackjack!"
    elif u_score == 0:
        return "You Won!, got a blackjack!"
    elif u_score > 21:
        return "you went over, you lose!"
    elif c_score > 21:
        return "Computer went over, you Won!"
    elif u_score > c_score:
        return "You Won!"
    else:
        return "You lose!"

def play_game():
    """Starts the game and deals 2 card each to the players, then check if players want to deal further."""
    print(logo)
    user_cards = []
    computer_cards = []
    user_score = -1
    computer_score = -1
    stop_game = False
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append((deal_card()))

    while not stop_game:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your hand is:{user_cards}, your current score:{user_score}")
        print(f"Computer first card:{computer_cards[0]},")
        if user_score == 0 or computer_score == 0 or user_score >21:
            stop_game = True
        else:
            user_should_deal = input("Do you want to play a game of Blackjack ?, 'y or 'n: ").lower()

            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                stop_game = True

    while computer_score != 0 and computer_score > 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"your final hand {user_cards}, you final score: {user_score}")
    print(f"computer final hand {computer_cards}, computer final score:{computer_score}")
    print(compare(user_score,computer_score))

while input("Do you want to play a game of Blackjack ?, 'y' or 'n': ") == 'y':
    print("\n" * 20)
    play_game()
