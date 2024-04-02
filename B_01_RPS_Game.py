# Create a game of Rock Paper Scissors

print(" Welcome to the game of Rock Paper Scissors")
# ask the user how many rounds he/she wants to play

# ask if they want to see the instructions

import random

def play_round(player_choice):
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    print("You chose:", player_choice)
    print("Computer chose:", computer_choice)

    if player_choice == computer_choice:
        return "It's a tie!"
    elif (
        (player_choice == "rock" and computer_choice == "scissors") or
        (player_choice == "paper" and computer_choice == "rock") or
        (player_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"


def play_game():
    print("Welcome to Rock-Paper-Scissors!")
    num_rounds = int(input("How many rounds do you want to play? "))
    player_score = 0
    computer_score = 0
    rounds_table = []

    for round_num in range(1, num_rounds + 1):
        print("------------------------------")
        player_choice = input("Enter your choice (rock, paper, or scissors): ")

        while player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please try again.")
            player_choice = input("Enter your choice (rock, paper, or scissors): ")

        result = play_round(player_choice)
        print(result)

        if result == "You win!":
            player_score += 1
        elif result == "Computer wins!":
            computer_score += 1
          
 print("------------------------------")
    print("Game over!")
    print("Player score:", player_score)
    print("Computer score:", computer_score)
    print("------------------------------")
print("End Results:")
for round in rounds_table:
    print(f"Round {round[0]} - Computer: {round[1]}, Player: {round[2]}, Result: {round[3]}")

play_game()
