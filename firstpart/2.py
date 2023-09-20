# Импортирование библиотеки
import random

# Создание класса с выбором и счетом
class Game:
    def __init__(self):
        self.choices = ["Камень", "Ножницы", "Бумага"]
        self.player_score = 0
        self.computer_score = 0

# Создание функции игры
    def game(self):
        while True:
            player_choice = input("Выберите: \n1-Камень\n2-Ножницы\n3-Бумага \n ")
            computer_choice = random.choice(self.choices)

            print(f"Вы выбрали {player_choice}")
            print(f"Компьютер выбрал {computer_choice}")

            if player_choice.capitalize() == computer_choice:
                print("Ничья!")
            elif (
                (player_choice == "Камень" and computer_choice == "Ножницы")
                or (player_choice == "Бумага" and computer_choice == "Камень")
                or (player_choice == "Ножницы" and computer_choice == "Бумага")
            ):
                print("Вы победили!")
                self.player_score += 1
            else:
                print("Вы проиграли!")
                self.computer_score += 1

            print(f"Вы: {self.player_score}")
            print(f"Компьютер: {self.computer_score}")

            play_again = input("Вы ходите сыграть снова? (да/нет):\n ")
            if play_again.lower() != "да":
                break


# Запуск игры
play = Game()
play.game()
