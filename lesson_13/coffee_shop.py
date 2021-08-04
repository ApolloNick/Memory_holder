import csv


class Store:
    def __init__(self):
        self.data = []
        self.balance = 0
        self.sell_list = []

    def import_products(self, length=4):
        with open("inventory.csv", "r+", encoding="UTF-8") as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            for row in csv_reader:
                self.data.append(row)
                if len(self.data) > length:
                    break
        return self.data

    def return_products(self, kind=None):
        list_of_products = []
        for line in self.data:
            if line[1] == kind:
                list_of_products.append(line)
            else:
                list_of_products.append(line)
        return list_of_products

    def overall_sum(self):
        sum_ = []
        for line in self.data:
            sum_.append(int(line[2]))
        return sum(sum_)

    def sell_product(self, name, kind, price):
        self.sell_list = [name, kind, price]
        for line in self.data:
            if self.sell_list == line:
                self.data.remove(line)
                self.balance += int(line[2])
        return self.data

    def count_income(self):
        income_list = []
        if self.sell_list[1] == "coffee" or self.sell_list[1] == "tea":
            if income_list != self.sell_list:
                income_list.append(int(self.sell_list[2]))
        return income_list

    def get_balance(self):
        return self.balance


class Product(Store):
    def __init__(self, name: str, kind: str, price: str):
        super().__init__()
        self.name = name
        self.kind = kind
        self.price = price
        self.balance = 0
        self.data = []

    def print(self):
        display_list = []
        for line in self.data:
            if line[0] == self.name and line[1] == self.kind and line[2] == self.price:
                display_list.append(line)
        return f"{display_list[0][0]}: {display_list[0][1]}, price: {display_list[0][2]} grn"


prod = Product('Earl Grey', 'tea', '25')
one = Store()
one.import_products(length=10)
print(one.sell_product('Earl Grey', 'tea', '25'))
print(one.get_balance())
print(one.count_income())

