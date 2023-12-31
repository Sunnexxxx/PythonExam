import random


class Game:
    def __init__(self, min_num, max_num):
        self.min_num = min_num
        self.max_num = max_num
        self.target_num = random.randint(min_num, max_num)
        self.num_attempts = 0

    def play(self):
        while True:
            guess = int(input(f"Угадайте число между {self.min_num} и {self.max_num}: "))
            self.num_attempts += 1

            if guess < self.target_num:
                print("Больше!")
            elif guess > self.target_num:
                print("Меньше!")
            else:
                print(f"Поздравляю!Вы угадали число за {self.num_attempts} попыток.")
                break


game = Game(1, 100)
game.play()
