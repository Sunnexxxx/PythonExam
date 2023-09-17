class Question:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def display_question(self):
        print(self.question)
        for i, choice in enumerate(self.choices):
            print(f"{i+1}. {choice}")

    def check_answer(self, user_answer):
        return user_answer == self.answer


class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def play(self):
        for question in self.questions:
            question.display_question()
            user_answer = int(input("Enter your answer (1-4): "))
            if question.check_answer(user_answer):
                print("Correct!")
                self.score += 1
            else:
                print("Incorrect!")
            print()

        print(f"Quiz completed! Your score is {self.score}/{len(self.questions)}.")


# Usage example
questions = [
    Question("What is the capital of France?", ["Paris", "London", "Berlin", "Rome"], 1),
    Question("What is the largest planet in our solar system?", ["Jupiter", "Saturn", "Mars", "Earth"], 1),
    Question("Who painted the Mona Lisa?", ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh", "Michelangelo"], 1),
    Question("What is the chemical symbol for gold?", ["Au", "Ag", "Fe", "Cu"], 1),
]


game = QuizGame(questions)
game.play()
