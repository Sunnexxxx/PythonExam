import random


class NumberGuessingGame:
    def __init__(self, min_num, max_num):
        self.min_num = min_num
        self.max_num = max_num
        self.target_num = random.randint(min_num, max_num)
        self.num_attempts = 0

    def play(self):
        while True:
            guess = int(input(f"Guess a number between {self.min_num} and {self.max_num}: "))
            self.num_attempts += 1

            if guess < self.target_num:
                print("Too low!")
            elif guess > self.target_num:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed the number in {self.num_attempts} attempts.")
                break



game = NumberGuessingGame(1, 100)
game.play()
