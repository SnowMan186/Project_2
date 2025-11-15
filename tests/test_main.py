import unittest
from src.category import Category
from src.product import Product, Smartphone, LawnGrass
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

    def test_display_info(self):
        """Проверка отображения информации о продукте."""
        product = Product("Телефон", "Простой телефон", 10000.0, 5)
        expected_info = "Название: Телефон, Цена: 10000.00 руб., Количество: 5 шт."
        self.assertEqual(product.display_info(), expected_info)

    def test_smartphone_display_info(self):
        """Проверка отображения информации о смартфоне."""
        smartphone = Smartphone("Galaxy S23", "Описание",
                                180000.0, 5, 95.5, "S23", 256, "Black")
        expected_info = ("Название: Galaxy S23, Цена: 180000.00 руб.,"
                         " Количество: 5 шт.\nМодель: S23, Энергоэффективность: 95.5%")
        self.assertEqual(smartphone.display_info(), expected_info)

    def test_lawngrass_display_info(self):
        """Проверка отображения информации о газонной траве."""
        lawngrass = LawnGrass("Газонная трава", "Описание",
                              500.0, 20, "Россия", "7 дней", "Зелёный")
        expected_info = ("Название: Газонная трава, Цена: 500.00 руб.,"
                         " Количество: 20 шт.\nСтрана производства: Россия, Период всхожести: 7 дней")
        self.assertEqual(lawngrass.display_info(), expected_info)

    def test_repr(self):
        product = Product('Test Product', 'Description', 1000.0, 10)
        repr_str = repr(product)
        self.assertTrue('<Product' in repr_str and 'Test Product' in repr_str)


class TestCategory(unittest.TestCase):
    def test_add_product_method(self):
        """Проверка метода добавления товара в категорию."""
        category = Category('Электроника', '', [])
        product = Product('Ноутбук', '', 50000.0, 3)
        category.add_product(product)
        self.assertEqual(len(category._products), 1)
        self.assertEqual(Category._product_count, 1)

    def test_products_getter(self):
        """Проверка геттера списка товаров."""
        category = Category('Электронные товары', '', [
            Product('Монитор', '', 15000.0, 10),
            Product('Колонки', '', 3000.0, 5)
        ])
        expected_output = (
            "Монитор, 15000.00 руб., остаток: 10 шт.\n"
            "Колонки, 3000.00 руб., остаток: 5 шт."
        )
        self.assertEqual(category.products, expected_output)


class TestNewFunctionality(unittest.TestCase):

    def test_new_product_class_method(self):
        """
        Проверка нового функционала по созданию продукта
        """
        params = {'name': 'Новую модель телефона', 'description': 'Самый новый смартфон', 'price': 120000.0,
                  'quantity': 10}
        product = Product.new_product(params)
        self.assertEqual(product.name, 'Новую модель телефона')
        self.assertEqual(product.price, 120000.0)
        self.assertEqual(product.quantity, 10)

    def test_total_cost_in_category(self):
        """
        Проверка суммы стоимости всех товаров в категории
        """
        product1 = Product("Notebook Acer", "16 ГБ RAM", 30000.0, 10)
        product2 = Product("Monitor LG", "IPS матрица", 15000.0, 5)
        category = Category("Компьютеры", "Все компьютерные аксессуары", [product1])
        category.add_product(product2)
        final_sum = (product1.price * product1.quantity) + (product2.price * product2.quantity)
        calculated_sum = sum([p.price * p.quantity for p in category._products])
        self.assertAlmostEqual(final_sum, calculated_sum)

    def setUp(self):
        self.smartphone = Smartphone("Galaxy S23", "", 180000.0, 5, 95.5, "S23", 256, "Black")
        self.lawn_grass = LawnGrass("Газонная трава", "", 500.0, 20, "Россия", "7 дней", "Green")

    def test_create_product(self):
        product = Product("Apple iPhone", "Описание", 150000.0, 10)
        self.assertIsInstance(product, Product)
        self.assertEqual(product.name, "Apple iPhone")
        self.assertEqual(product.price, 150000.0)
        self.assertEqual(product.quantity, 10)

    def test_smartphone_attributes(self):
        self.assertEqual(self.smartphone.efficiency, 95.5)
        self.assertEqual(self.smartphone.model, "S23")
        self.assertEqual(self.smartphone.memory, 256)
        self.assertEqual(self.smartphone.color, "Black")

    def test_lawn_grass_attributes(self):
        self.assertEqual(self.lawn_grass.country, "Россия")
        self.assertEqual(self.lawn_grass.germination_period, "7 дней")
        self.assertEqual(self.lawn_grass.color, "Green")

    def test_product_addition(self):
        another_phone = Smartphone("iPhone X", "", 120000.0, 3, 90.0, "X", 128, "White")
        result = self.smartphone + another_phone
        self.assertEqual(result, 1260000.0)

    def test_type_error_on_mixed_addition(self):
        with self.assertRaises(TypeError):
            self.smartphone + self.lawn_grass

    def test_adding_to_category(self):
        category = Category("Каталог", "Продукты", [])
        category.add_product(self.smartphone)
        self.assertIn(self.smartphone, category._products)

    def test_wrong_type_in_category(self):
        with self.assertRaises(TypeError):
            category = Category("Каталог", "Продукты", [])
            category.add_product("Некорректный объект")


if __name__ == '__main__':
    unittest.main()
