import unittest
from src.main import Product, Category, load_data_from_json


class TestProduct(unittest.TestCase):
    def test_product_initialization(self):
        p = Product("Test Phone", "Description of phone", 10000.0, 10)
        self.assertEqual(p.name, "Test Phone")
        self.assertEqual(p.description, "Description of phone")
        self.assertEqual(p.price, 10000.0)
        self.assertEqual(p.quantity, 10)


class TestCategory(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Очистка глобального состояния перед всеми тестами"""
        Category.category_count = 0
        Category.product_count = 0

    def setUp(self):
        """Подготовка данных для каждого отдельного теста"""
        self.p1 = Product("Phone A", "Desc A", 15000.0, 5)
        self.p2 = Product("Phone B", "Desc B", 20000.0, 10)
        self.cat = Category("Телефоны", "Раздел телефонов", [self.p1, self.p2])

    def test_category_initialization(self):
        self.assertEqual(self.cat.name, "Телефоны")
        self.assertEqual(self.cat.description, "Раздел телефонов")
        self.assertEqual(len(self.cat.products), 2)
        self.assertEqual(Category.category_count, 1)

    def test_load_data_from_json(self):
        categories = load_data_from_json('data.json')
        self.assertIsInstance(categories, list)
        self.assertGreater(len(categories), 0)
        first_cat = categories[0]
        self.assertEqual(first_cat.name, "Смартфоны")
        self.assertEqual(len(first_cat.products), 3)


if __name__ == '__main__':
    unittest.main()
