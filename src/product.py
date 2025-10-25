class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, params_dict: dict, existing_products=None):
        name = params_dict.get('name', '')
        desc = params_dict.get('description', '')
        price = params_dict.get('price', 0.0)
        qty = params_dict.get('quantity', 0)

        if existing_products is not None:
            for existing_prod in existing_products:
                if existing_prod.name.lower().strip() == name.lower().strip():
                    existing_prod.quantity += qty
                    existing_prod.price = max(existing_prod.price, price)
                    return existing_prod

        return cls(name=name, description=desc, price=price, quantity=qty)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Ошибка: Цена не должна быть нулевой или отрицательной!")
            return

        old_price = self._price
        if new_price < old_price:
            confirm = input(
                f"Внимание! Вы пытаетесь снизить цену с {old_price:.2f} руб. "
                f"до {new_price:.2f} руб. Подтверждаете изменение? (y/n): "
            )
            if confirm.lower() != 'y':
                print("Изменение цены отменено.")
                return

        self._price = new_price
