class MadLibs:
    def __init__(self):
        self.one = ""
        self.two = ""
        self.three = ""
        self.four = ""

    def inputs(self):
        self.one = input("Введите язык программирования: ")
        self.two = input("Введите кол-во месяцев: ")
        self.three = input("Введите редактор кода: ")
        self.four = input("Введите имя учителя : ")

    def story(self):
        story = f"Я учу {self.one} в течении {self.two} месяцев и пишу на {self.three}, моего учителя зовут {self.four}."
        return story

madlibs = MadLibs()
madlibs.inputs()
story = madlibs.story()
print(story)