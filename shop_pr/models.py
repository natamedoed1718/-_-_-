from typing import List


class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __add__(self, other):
        if not isinstance(other, Product):
            return NotImplemented

        return self.price * self.quantity + other.price * other.quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

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

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    # приватный список продуктов
    def add_product(self, product):
        self.__products.append(product)
        Category.product_count += 1

    # декоратор
    @property
    def products(self):
        return self.__products

    @property
    def products_info(self):
        return "\n".join(str(product) for product in self.__products)


class CategoryIterator:
    def __init__(self, category: Category):
        self._products = category.products
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._products):
            product = self._products[self._index]
            self._index += 1
            return product
        raise StopIteration
