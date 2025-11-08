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
        total_quantity = sum([p.quantity for p in self._products])
        return f"{self.name}, всего товаров: {total_quantity}"

    def add_product(self, product: 'Product'):
        if isinstance(product, Product):
            self._products.append(product)
            Category._product_count += 1
        else:
            raise TypeError("Можно добавлять только объекты класса Product или его потомков")

    @property
    def products(self):
        result = ""
        for product in self._products:
            result += f"{product}\n"
        return result.strip()
