from abc import ABC, abstractmethod
from src.log_mixin import LogMixin

class Product(ABC):
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @abstractmethod
    def display_info(self):
        pass

    @classmethod
    def new_product(cls, params_dict: dict):
        return cls(**params_dict)


class Smartphone(LogMixin, Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 efficiency: float, model: str, memory: int, color: str):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def display_info(self):
        return (f"Название: {self.name}, Модель: {self.model}, Цена: {self.price:.2f} руб.,"
                f" Количество: {self.quantity} шт.")


class LawnGrass(LogMixin, Product):
    def __init__(self, name: str, description: str, price: float,
                 quantity: int, country: str, germination_period: str, color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def display_info(self):
        return (f"Название: {self.name}, Страна производства: {self.country},"
                f" Цена: {self.price:.2f} руб., Количество: {self.quantity} шт.")
