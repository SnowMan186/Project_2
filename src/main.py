import json


class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name            # Название продукта
        self.description = description   # Описание продукта
        self.price = price          # Цена продукта
        self.quantity = quantity    # Количество на складе


class Category:
    category_count = 0  # Общий счётчик созданных категорий
    product_count = 0  # Общий счётчик продуктов во всех категориях

    def __init__(self, name: str, description: str, products: list):
        self.name = name  # Название категории
        self.description = description  # Описание категории
        self.products = products  # Список продуктов категории

        # Автоматическое обновление общих счётчиков
        Category.category_count += 1  # Добавляем категорию
        Category.product_count += len(self.products)  # Добавляем количество продуктов


# Создаем первые три продукта
product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
product2 = Product("iPhone 15 Pro Max", "512GB, Deep Purple", 210000.0, 8)
product3 = Product("Xiaomi Redmi Note 11", "128GB, Blue", 31000.0, 14)

# Создаем первую категорию
category1 = Category("Смартфоны", "Самые современные смартфоны", [product1, product2, product3])

print(f"Количество категорий: {Category.category_count}")  # Выведет: 1
print(f"Общее количество товаров: {Category.product_count}")  # Выведет: 3

# Создаем ещё один товар и вторую категорию
product4 = Product("LG OLED TV", "55 дюймов, 4K HDR", 123000.0, 7)
category2 = Category("Телевизоры", "Современные телевизоры", [product4])

print(f"Количество категорий: {Category.category_count}")  # Выведет: 2
print(f"Общее количество товаров: {Category.product_count}")  # Выведет: 4


# Вспомогательная функция для загрузки данных из JSON
def load_data_from_json(file_path: str):
    with open(file_path, encoding='utf-8') as file:
        data = json.load(file)
        categories = []
        for item in data:
            products_list = []
            for prod in item['products']:
                p = Product(prod['name'], prod['description'], prod['price'], prod['quantity'])
                products_list.append(p)

            cat = Category(item['name'], item['description'], products_list)
            categories.append(cat)
        return categories


categories = load_data_from_json('data.json')

# Запуск примера
if __name__ == "__main__":
    categories = load_data_from_json("data.json")
    for cat in categories:
        print(f"Категория: {cat.name}")
        print(f"Товары: {[prod.name for prod in cat.products]}")
