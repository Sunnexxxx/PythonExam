import random

class Hangman:
    def __init__(self, word):
        self.word = word
        self.guesses = []
        self.max_attempts = 6

    def play(self):
        print("Добро пожаловать в висилицу!")
        print("Угадайте слово и победите в игру.")
        print("В слове", len(self.word), "буквы.")

        while True:
            self.display_word()

            if self.is_word_guessed():
                print("Поздравляю!Вы верно угадали слово.")
                break

            if len(self.guesses) >= self.max_attempts:
                print("ы проиграли! Ваши попытки закончились.")
                print("Слово было:", self.word)
                break

            guess = self.get_guess()
            self.guesses.append(guess)

            if guess not in self.word:
                print("Неправильно!")
                self.display_hangman(len(self.guesses))

    def display_word(self):
        for letter in self.word:
            if letter in self.guesses:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        print()

    def is_word_guessed(self):
        for letter in self.word:
            if letter not in self.guesses:
                return False
        return True

    def get_guess(self):
        while True:
            guess = input("Введите выши догадки: ").lower()
            if len(guess) != 1:
                print("Пожалуйста введите одну букву.")
            elif guess in self.guesses:
                print("Вы уже вводили эту букву.")
            elif not guess.isalpha():
                print("Пожалуйста введите букву.")
            else:
                return guess

    def display_hangman(self, attempts):
        stages = [
            """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |     / \\
               -
            """,
            """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |     / 
               -
            """,
            """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |      
               -
            """,
            """
               --------
               |      |
               |      O
               |     \\|
               |      |
               |     
               -
            """,
            """
               --------
               |      |
               |      O
               |      |
               |      |
               |     
               -
            """,
            """
               --------
               |      |
               |      O
               |    
               |      
               |     
               -
            """,
            """
               --------
               |      |
               |      
               |    
               |      
               |     
               -
            """
        ]
        print(stages[attempts])


word_list = ["пайтон", "виселица", "программирование", "код", "компьютер"]
words = random.choice(word_list)

game = Hangman(words)
game.play()
