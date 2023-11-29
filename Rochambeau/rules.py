import random

def play_game():
    options = ['rock', 'paper', 'scissors']
    player_score = 0
    opponent_score = 0

    while True:
        player_choice = input("Choose rock, paper, or scissors: ").lower()

        if player_choice not in options:
            print("Invalid option. Please choose rock, paper, or scissors.")
            continue

        opponent_choice = random.choice(options)

        print("Opponent chose:", opponent_choice)

        if player_choice == opponent_choice:
            print("It's a tie!")
        elif (player_choice == 'rock' and opponent_choice == 'scissors') or \
             (player_choice == 'scissors' and opponent_choice == 'paper') or \
             (player_choice == 'paper' and opponent_choice == 'rock'):
            print("You win!")
            player_score += 1
        else:
            print("You lose!")
            opponent_score += 1

        play_again = input("Do you want to play again? (yes/no): ").lower()

        if play_again != 'yes':
            break

    print("Game over!")
    print("Your score:", player_score)
    print("Opponent's score:", opponent_score)

play_game()
