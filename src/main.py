import json
from src.category import Category
from src.product import Product, Smartphone, LawnGrass

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
    with open(file_path, encoding='utf-8') as file:
        data = json.load(file)
        categories = []
        for item in data:
            products_list = []
            for prod in item['products']:
                p = Product(**prod)
                products_list.append(p)

            cat = Category(item['name'], item['description'], products_list)
            categories.append(cat)
        return categories


if __name__ == "__main__":
    smartphones = load_data_from_json("data.json")
    for cat in smartphones:
        print(f"КАТЕГОРИЯ: {cat.name}\nОПИСАНИЕ: {cat.description}\nТОВАРЫ:\n{cat.products}\n")
