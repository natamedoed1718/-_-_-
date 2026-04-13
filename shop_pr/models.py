from typing import List


class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        if isinstance(other, Product):
            return self.name == other.name
        return False

    @classmethod
    def new_product(cls, data: dict, products: list["Product"] | None = None):
        if products:
            for product in products:
                if product.name == data["name"]:
                    product.quantity += data["quantity"]
                    product.price = max(product.price, data["price"])
                    return product

        return cls(
            data["name"],
            data["description"],
            data["price"],
            data["quantity"],
        )

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if value < self.__price:
            answer = input("Вы уверены, что хотите понизить цену? (y/n): ")
            if answer != "y":
                return

        self.__price = value


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: List["Product"]):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    # приватный список продуктов
    def add_product(self, product):
        self.__products.append(product)
        Category.product_count += 1

    # декоратор
    @property
    def products(self):
        return self.__products
