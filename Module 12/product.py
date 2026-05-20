class Product:
    def __init__(self, product_id: int, name: str, price: float, quantity: int):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    def get_product_info(self) -> str:
        return f"ID: {self.__product_id}, Name: {self.__name}, Price: {self.__price}, Quantity: {self.__quantity}"

    def get_id(self) -> int:
        return self.__product_id

    def update_quantity(self, quantity: int) -> None:
        if quantity >= 0:
            self.__quantity = quantity
        else:
            raise ValueError("Quantity cannot be negative")

    def update_price(self, price: float) -> None:
        if price >= 0:
            self.__price = price
        else:
            raise ValueError("Price cannot be negative")

    def __str__(self) -> str:
        return self.get_product_info()
#kscm