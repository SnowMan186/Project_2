import json
from src.category import Category
from src.product import Product, Smartphone, LawnGrass
import logging

logging.basicConfig(level=logging.INFO)


# Создание товаров
smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256ГБ, Серый цвет, 200МП камера", 180000.0, 5, 95.5, "S23 Ultra",
                         256, "Серый")
smartphone2 = Smartphone("iPhone 15 Pro Max", "512ГБ, Глубокий фиолетовый", 210000.0, 8, 98.2, "Pro Max", 512,
                         "Deep purple")
lawn_grass1 = LawnGrass("Газонная трава", "Лучшая для сада", 500.0, 20, "Россия", "7 дней", "Зелёный")

# Категории товаров
category_smartphones = Category("Смартфоны", "Современнейшие гаджеты", [smartphone1, smartphone2])
category_lawn_grass = Category("Газонная трава", "Лучшие сорта", [lawn_grass1])


# Загрузка данных из JSON
def load_data_from_json(file_path: str):
    with open(file_path, 'r', encoding="utf-8") as file:
        data = json.load(file)
        categories = []

        for category_data in data:
            products = []
            for product_dict in category_data['products']:
                if category_data['name'] == 'Смартфоны':
                    product = Smartphone(**product_dict)
                elif category_data['name'] == 'Газонная трава':
                    product = LawnGrass(**product_dict)
                else:
                    product = Product(**product_dict)
                products.append(product)

            category = Category(category_data['name'], category_data['description'], products)
            categories.append(category)

    return categories


if __name__ == "__main__":
    # Создание экземпляров товаров
    smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                             "S23 Ultra", 256, "Серый")
    smartphone2 = Smartphone("iPhone 15 Pro Max", "512GB, Deep Purple", 210000.0, 8, 98.2, "Pro Max", 512,
                             "Deep Purple")
    lawn_grass1 = LawnGrass("Газонная трава", "Лучшая для сада", 500.0, 20, "Россия", "7 дней", "Зелёный")

    # Создание категорий товаров
    category_smartphones = Category("Смартфоны", "Современные гаджеты", [smartphone1, smartphone2])
    category_lawn_grass = Category("Газонная трава", "Лучшие сорта", [])

    # Добавляем товар в категорию газонных трав
    category_lawn_grass.add_product(lawn_grass1)

    # Выводим информацию о категориях и товарах внутри них
    print("Категория:", category_smartphones)
    print("Продукты в категории Смартфонов:\n", category_smartphones.products)

    print("\nКатегория:", category_lawn_grass)
    print("Продукты в категории Газонной травы:\n", category_lawn_grass.products)

    # Тестируем обработку неправильного добавления элемента
    try:
        category_smartphones.add_product("Некорректный объект")
    except TypeError as e:
        print("\nОшибка при добавлении товара:", e)

    # Добавляем новый товар в категорию Смартфонов
    new_smartphone = Smartphone("Google Pixel 8", "128 ГБ памяти, Черный", 80000.0, 10, 93.5, "Pixel 8", 128, "Черный")
    category_smartphones.add_product(new_smartphone)

    # Повторно выводим список товаров в категории Смартфонов
    print("\nОбновленные продукты в категории Смартфонов:\n", category_smartphones.products)

    # Проверяем общее количество товаров
    print("\nВсего товаров:", Category._product_count)

    # Примеры вычисления общей стоимости товаров путем перегрузки оператора '+'
    total_cost_smartphones = smartphone1 + smartphone2
    print("\nОбщая стоимость смартфонов:", total_cost_smartphones)

    # Попытка сложения разнотипных товаров
    try:
        mixed_total = smartphone1 + lawn_grass1
    except TypeError as e:
        print("\nОшибка при сложении разнотипных товаров:", e)
