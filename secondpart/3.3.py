class Question:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def my_questions(self):
        print(self.question)
        for i, choice in enumerate(self.choices):
            print(f"{i+1}. {choice}")

    def check(self, user_answer):
        return user_answer == self.answer


class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def play(self):
        for question in self.questions:
            question.my_questions()
            user_answer = int(input("Введите ваш ответ (1-4):"))
            if question.check(user_answer):
                print("Верно!")
                self.score += 1
            else:
                print("Неверно!")
            print()

        print(f"Викторина окончена! Ваш счёт: {self.score}/{len(self.questions)}.")


questions = [
    Question("Что такое while?", ["Функция", "Цикл", "Свойство", "Класс"], 2),
    Question("Какая команда запускает код?", ["Shift+Alt", "Ctrl+Alt", "Sift+F10", "Ctrl+F12"], 3),
    Question("Какая команда создаёт функцию?", ["def", "for", "len", "print"], 1),
    Question("Что делает commit?", ["Отправляет", "Удаляет", "Обновляет", "Применяет изменения"], 4),
]

game = QuizGame(questions)
game.play()
