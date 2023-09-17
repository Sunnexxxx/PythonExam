import random


class RockPaperScissors:
    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]
        self.player_score = 0
        self.computer_score = 0

    def play_game(self):
        while True:
            player_choice = input("Enter your choice: \n1-rock\n2-paper\n3-scissors ")
            computer_choice = random.choice(self.choices)

            print(f"Player chooses {player_choice}")
            print(f"Computer chooses {computer_choice}")

            if player_choice == computer_choice:
                print("It's a tie!")
            elif (
                (player_choice == "rock" and computer_choice == "scissors")
                or (player_choice == "paper" and computer_choice == "rock")
                or (player_choice == "scissors" and computer_choice == "paper")
            ):
                print("Player wins!")
                self.player_score += 1
            else:
                print("Computer wins!")
                self.computer_score += 1

            print(f"Player score: {self.player_score}")
            print(f"Computer score: {self.computer_score}")

            play_again = input("Do you want to play again? (y/n): ")
            if play_again.lower() != "y":
                break


game = RockPaperScissors()
game.play_game()
