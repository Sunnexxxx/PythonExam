class MadLibs:
    def __init__(self):
        self.noun = ""
        self.verb = ""
        self.adjective = ""
        self.adverb = ""

    def get_inputs(self):
        self.noun = input("Введите существительное: ")
        self.verb = input("Введите глагол: ")
        self.adjective = input("Введите прилагательное: ")
        self.adverb = input("Введите наречие: ")

    def generate_story(self):
        story = f"{self.adjective} {self.noun} {self.verb} {self.adverb}."
        return story

madlibs_game = MadLibs()
madlibs_game.get_inputs()
story = madlibs_game.generate_story()
print(story)