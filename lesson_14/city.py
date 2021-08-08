import random
from faker import Faker
faker = Faker()


class City:
    """Description of structure of whole city"""

    def __init__(self):
        # Как сделать так чтобы добавляло именно по 4 элемента в строку
        self.structure = []
        self.population = 0
        self.count = 0

    def add_street(self, name_of_street: str = " "):
        if name_of_street == " ":
            name_of_street = faker.name()
        amount_of_houses = random.randint(5, 20)
        self.count += 1
        return self.structure.extend([name_of_street, amount_of_houses])

    def delete_street(self, name_of_street: str):
        return self.structure.remove(name_of_street)

    def add_house(self, number_of_house: int = 0):
        # number_of_house += 1  Почему нельзя сделать учет добавления дома инкрементом?
        number_of_house = random.randint(1, 10)
        amount_of_population = random.randint(5, 20)
        self.population += amount_of_population
        return self.structure.extend([number_of_house, amount_of_population])

    def delete_house(self, number_of_house: int):
        return self.structure.pop(number_of_house)

    def fill_up(self):
        self.add_street()
        self.add_house()
        return self.structure

    def count_of_population(self):
        return self.population

    def column_print(self):
        for _ in range(self.count):
            print(str(self.structure[:4]).rjust(50))


class Street:
    """Description of street"""
    def __init__(self):
        self.streets = []

    def add_street(self, name_of_street: str = " "):
        if name_of_street == " ":
            name_of_street = faker.name()
        amount_of_houses = random.randint(5, 20)
        return self.streets.append([name_of_street, amount_of_houses])

    def delete_street(self, name_of_street: str):
        return self.streets.remove(name_of_street)

    def print_street(self):
        return self.streets


class House:
    """Description of house"""
    def __init__(self):
        self.list_of_houses = []
        self.population = 0

    def add_house(self, number_of_house: int = 0):
        if number_of_house == 0:
            number_of_house = random.randint(5, 20)
        population = random.randint(5, 20)
        return self.list_of_houses.append([number_of_house, population])

    def delete_house(self, number_of_house: int):
        return self.list_of_houses.remove(number_of_house)

    def print_houses(self):
        return self.list_of_houses


city_1 = City()
city_1.fill_up()
print(city_1.fill_up())
city_1.column_print()







