from src.base_product import Product
from src.log_mixin import LogMixin


class Product(LogMixin):
    def __init__(self, name: str, description: str, price: float, quantity: int):
        super().__init__(name, description, price, quantity)

class Product(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    def __str__(self):
        """Стрковое представления продукта"""
        return f"{self.name}, {self.price:.2f} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Суммирует общую стоимость двух товаров на складее
        Формула: цена * количествол первого товара + цена * количество второго товара"""
        if type(other) != type(self):
            raise TypeError("Нельзя складывать товары разного типа")
        return self.price * self.quantity + other.price * other.quantity

    def display_info(self):
        """Методом отображается информация о продукте."""
        return f"Название: {self.name}, Цена: {self.price:.2f} руб., Количество: {self.quantity} шт."

    @classmethod
    def new_product(cls, params_dict: dict, existing_products=None):
        name = params_dict.get('name', '').lower().strip()
        desc = params_dict.get('description', '')
        price = params_dict.get('price', 0.0)
        qty = params_dict.get('quantity', 0)

        if existing_products is not None:
            for existing_prod in existing_products:
                if existing_prod.name.lower().strip() == name:
                    existing_prod.quantity += qty
                    existing_prod.price = price
                    return existing_prod

        return cls(name=name.capitalize(), description=desc, price=price, quantity=qty)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Ошибка: Цена не должна быть нулевой или отрицательной!")
            return
        self._price = new_price

        old_price = self._price
        if new_price < old_price:
            confirm = input(
                f"Внимание! Вы пытаетесь снизить цену с {old_price:.2f} руб. до {new_price:.2f} руб." +
                "\nПодтверждаете изменение? (y/n): "
            )
            if confirm.lower() != 'y':
                print("Изменение цены отменено.")
                return

        self._price = new_price


class Smartphone(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 efficiency: float, model: str, memory: int, color: str):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def display_info(self):
        """Расширенный метод отображения информации для смартфонов."""
        basic_info = super().display_info()
        additional_info = f"\nМодель: {self.model}, Энергоэффективность: {self.efficiency}%"
        return basic_info + additional_info


class LawnGrass(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country: str, germination_period: str, color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def display_info(self):
        """Расширенный метод отображения информации для газонной травы."""
        basic_info = super().display_info()
        additional_info = f"\nСтрана производства: {self.country}, Период всхожести: {self.germination_period}"
        return basic_info + additional_info


if __name__ == "__main__":
    product = Product('Продукт1', 'Описание продукта', 1200, 10)
    print(product.display_info())
