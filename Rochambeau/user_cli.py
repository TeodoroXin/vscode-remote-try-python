
from rules import determine_winner

def play_game():
    player_score = 0
    computer_score = 0

    while True:
        print("Choose one of the following options:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")

        choice = input("Enter your choice (1-3): ")

        if choice not in ["1", "2", "3"]:
            print("Invalid option. Please choose a valid option.")
            continue

        player_choice = int(choice)
        computer_choice = determine_computer_choice()

        print("You chose:", get_choice_name(player_choice))
        print("Computer chose:", get_choice_name(computer_choice))

        winner = determine_winner(player_choice, computer_choice)

        if winner == "player":
            player_score += 1
            print("You win!")
        elif winner == "computer":
            computer_score += 1
            print("Computer wins!")
        else:
            print("It's a tie!")

        print("Player score:", player_score)
        print("Computer score:", computer_score)

        play_again = input("Do you want to play again? (yes/no): ")

        if play_again.lower() != "yes":
            break

def determine_computer_choice():
    # Logic to determine computer's choice (rock, paper, or scissors)
    # ...

def get_choice_name(choice):
    if choice == 1:
        return "Rock"
    elif choice == 2:
        return "Paper"
    elif choice == 3:
        return "Scissors"
    else:
        return "Unknown"

play_game()
