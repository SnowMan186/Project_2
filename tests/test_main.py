import unittest
from src.category import Category
from src.product import Product
from unittest.mock import patch


class TestProduct(unittest.TestCase):

    def test_new_product_creation(self):
        # Проверка создания нового товара
        params = {
            'name': 'Телефон',
            'description': 'Новый смартфон',
            'price': 10000.0,
            'quantity': 10
        }
        product = Product.new_product(params)
        self.assertEqual(product.name, 'Телефон')
        self.assertEqual(product.price, 10000.0)
        self.assertEqual(product.quantity, 10)

    def test_duplicate_product_handling(self):
        # Проверка обработки дублирующих товаров
        existing_products = [
            Product('Телефон', '', 10000.0, 10),
            Product('Планшет', '', 20000.0, 5)
        ]
        duplicate_params = {
            'name': 'телефон',
            'description': '',
            'price': 12000.0,
            'quantity': 5
        }
        updated_product = Product.new_product(duplicate_params, existing_products)
        self.assertEqual(updated_product.quantity, 15)
        self.assertEqual(updated_product.price, 12000.0)

    def test_price_setter_protection(self):
        # Проверка защиты от неправильной установки цены
        product = Product('Телефон', '', 10000.0, 10)
        product.price = -5000.0
        self.assertEqual(product.price, 10000.0)

        # Проверка снижения цены с подтверждением
        with patch('builtins.input', return_value='y'):
            product.price = 8000.0
        self.assertEqual(product.price, 8000.0)


class TestCategory(unittest.TestCase):

    def test_add_product_method(self):
        # Проверка метода добавления товара в категорию
        category = Category('Электроника', '', [])
        product = Product('Ноутбук', '', 50000.0, 3)
        category.add_product(product)
        self.assertEqual(len(category._products), 1)
        self.assertEqual(Category._product_count, 1)

    def test_products_getter(self):
        # Проверка геттера списка товаров
        category = Category('Электронные товары', '', [
            Product('Монитор', '', 15000.0, 10),
            Product('Колонки', '', 3000.0, 5)
        ])
        expected_output = (
            "Монитор, 15000.00 руб. Остаток: 10 шт.\n"
            "Колонки, 3000.00 руб. Остаток: 5 шт."
        )
        self.assertEqual(category.products, expected_output)


if __name__ == '__main__':
    unittest.main()
