# Rock-Paper-Scissors Tournament


import random

moves = ["rock", "paper", "scissors"]

while True:

    user_score = 0
    computer_score = 0

    for round_num in range(1, 6):

        print("\nRound", round_num)

        user = input("Enter rock, paper, or scissors: ")

        while user not in moves:
            user = input("Invalid input. Enter again: ")

        computer = moves[random.randint(0, 2)]

        print("Computer chose:", computer)

        if user == computer:
            print("Draw")

        elif (
            (user == "rock" and computer == "scissors") or
            (user == "paper" and computer == "rock") or
            (user == "scissors" and computer == "paper")
        ):
            print("You win this round")
            user_score += 1

        else:
            print("Computer wins this round")
            computer_score += 1

    print("\nFinal Score")
    print("You:", user_score)
    print("Computer:", computer_score)

    if user_score > computer_score:
        print("You are the overall winner!")

    elif computer_score > user_score:
        print("Computer is the overall winner!")

    else:
        print("Tournament draw!")

    replay = input("Play again? (yes/no): ")

    if replay != "yes":
        break