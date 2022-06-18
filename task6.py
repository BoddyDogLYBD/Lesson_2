"""
Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах.
Реализовать словарь, в котором каждый ключ — характеристика товара, например название,
а значение — список значений-характеристик, например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
"""
"""raiting = []
database = {
    "name": [],
    "cost": [],
    "number": [],
    "equal": []
}

counter = 1
while True:
    name = input("Введите название товара: ")
    cost = int(input("Введите цену товара: "))
    number = int(input("Введите кол-во товара: "))
    equal = input("Введите меру измерения: ")
    params = {
        "name" : name,
        "cost" : cost,
        "number" : number,
        "equal" : equal
    }

    thing = (counter, params)
    raiting.append(thing)

    for key, value in params.items():
        i = database.get(key)
        if value in i:
            continue
        i.append(value)
        continue

    counter += 1
    exit_answer = input('Ввести еще позицию? Ответьте "Да"/"Нет"').lower()
    if exit_answer == "нет":
        break
print(database)"""

products = []
for i in range(1, 4):
    print(f"Заполняем информацию по {i}-му товару")
    product_name = input("Название: ")
    product_price = int(input("Цена: "))
    product_count = int(input("Количество: "))
    product_measure =  input("Единица измерения: ")
    products.append((i, {'название': product_name, 'цена': product_price, 'количество': product_count, 'eд': product_measure}))

print(f"Исходный список товаров: \n{products}")

product_names = []
product_prices = []
product_counts = []
product_measures = []
for i in products:
    product_names.append(i[1].get('название'))
    product_prices.append(i[1].get('цена'))
    product_counts.append(i[1].get('количество'))
    product_measures.append(i[1].get('eд'))

report = {
    'название': list(set(product_names)),
    'цена': list(set(product_prices)),
    'количество': list(set(product_counts)),
    'eд': list(set(product_measures))
}

print(f"Отчет по списку товаров: \n{report}")