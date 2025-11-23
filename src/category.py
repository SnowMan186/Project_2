from src.product import Product


class Category:
    _category_count = 0
    _product_count = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self._products = products

        Category._category_count += 1
        Category._product_count += len(self._products)

    def __str__(self):
        total_quantity = sum(p.quantity for p in self._products)
        return f"{self.name}, всего товаров: {total_quantity}"

    def add_product(self, product):
        if isinstance(product, Product):
            self._products.append(product)
            Category._product_count += 1
        else:
            raise TypeError("Можно добавлять только объекты класса Product или его потомков")

    @property
    def products(self):
        result = ""
        for product in self._products:
            result += f"{product.name}, {product.price:.2f} руб., остаток: {product.quantity} шт.\n"
        return result.strip()

    def middle_price(self):
        try:
            total_price = sum(product.price for product in self._products)
            average_price = total_price / len(self._products)
            return round(average_price, 2)
        except ZeroDivisionError:
            return 0
