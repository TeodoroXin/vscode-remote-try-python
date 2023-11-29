import random
from rules import determine_winner

def play_game():
    score = 0
    play_again = True

    while play_again:
        user_choice = input("Choose rock, paper, or scissors: ").lower()

        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid option. Please choose rock, paper, or scissors.")
            continue

        opponent_choice = random.choice(["rock", "paper", "scissors"])
        result = determine_winner(user_choice, opponent_choice)

        if result == "win":
            score += 1
            print("You won!")
        elif result == "lose":
            print("You lost!")
        else:
            print("It's a tie!")

        play_again = input("Do you want to play again? (yes/no): ").lower() == "yes"

    print("Game over. Your score:", score)

if __name__ == "__main__":
    play_game()
