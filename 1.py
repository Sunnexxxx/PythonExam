class Pizza:
    def __init__(self, name, toppings, crust, price):
        self.name = name
        self.toppings = toppings
        self.crust = crust
        self.price = price

    def __str__(self):
        return f'Название: {self.name}\nДобавки: {", ".join(self.toppings)}\nТесто: {self.crust}\nЦена: {self.price}'

    def __repr__(self):
        return f"{self.name}: {self.toppings}"


# Список пицц
pizzas = [
    Pizza("Пепперони", ["сыр", "колбаса пепперони"], "тонкое", 80000),
    Pizza("Барбекю", ["сыр", "бекон", "помидоры"], "среднее", 70000),
    Pizza("Дары моря", ["сыр", "креветки", "кальмары", "лосось"], "толстое", 50000),
]

# Список начинок
toppings = ["картошка", "колбаса", "бекон", "грибы", "рыба", "кальмары", "лосось", ""]

# Список тестов
crusts = ["тонкое", "среднее", "толстое"]

# Класс заказа
class Order:
    def __init__(self):
        self.pizzas = []

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)

    def calculate_price(self):
        total_price = 0
        for pizza in self.pizzas:
            total_price += pizza.price
        return total_price

# Основная функция
def main():
    total_price = 0
    while True:
        # Создаем новый заказ
        order = Order()

        # Выбираем пиццу
        pizza = choose_pizza()
        order.add_pizza(pizza)

        # Выбираем начинку
        toppings = choose_toppings()
        pizza.toppings += toppings

        # Выбираем тесто
        crust = choose_crust()
        pizza.crust = crust

        # Рассчитываем стоимость заказа
        total_price += order.calculate_price()

        # Выводим информацию о заказе
        print("Добавлен заказ:")
        for pizza in order.pizzas:
            print(pizza)
        print(f"Итоговая цена: {total_price}")

        # Повторный заказ

        answer = input("Заказать еще? (да/нет): ")

        if answer.lower() == "нет":
            break

# Функция для выбора пиццы
def choose_pizza():
    print("Выберите пиццу:")
    for i, pizza in enumerate(pizzas):
        print(f"{i + 1}. {pizza.name}")
    pizza_id = input("Введите номер пиццы: ")
    pizza_id = int(pizza_id) - 1
    return pizzas[pizza_id]

# Функция для выбора начинки
def choose_toppings():
    print("Выберите начинку:")
    for i, topping in enumerate(toppings):
        print(f"{i + 1}. {topping}")
    toppings_list = []
    while True:
        topping_id = input("Введите номер начинки (0 - для завершения): ")
        topping_id = int(topping_id) - 1
        if topping_id == -1:
            break
        toppings_list.append(toppings[topping_id])
    return toppings_list

# Функция для выбора теста
def choose_crust():
    print("Выберите тесто:")
    for i, crust in enumerate (crusts):
        print(f"{i + 1}. {crust}")
    crust_id = input("Введите номер теста: ")
    crust_id = int(crust_id) - 1
    return crusts[crust_id]

if __name__ == '__main__':
    main()
