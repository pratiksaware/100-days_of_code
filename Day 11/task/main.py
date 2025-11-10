import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

computer_score = 0
player_score = 0
blackjack = 21

#Draw cards
com_hand = random.sample(cards,2)
player_hand = random.sample(cards,2)

#calculate score
computer_score += com_hand[0] + com_hand[1]
player_score += player_hand[0] + player_hand[1]

def check_blackjack(user1, user2):
    print(f"Computer hand: {com_hand[0]}")
    print(f"your hand: {player_hand}")
    print(f"computer score = {user1}\nPlayer score = {user2}")
    if computer_score == 21 and player_score == 21:
        print("It's a blackjack for computer, you loose")
    elif computer_score == 21:
        print("It's a blackjack for computer, you loose")
    elif player_score == 21:
        print("you  got a blackjack !, you Won.")
    elif computer_score < player_score:
        print("you win!")
    elif computer_score > player_score:
        print("Computer won")



check_blackjack(computer_score,player_score)