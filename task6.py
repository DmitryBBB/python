print("Программа инвентаризации склада магазина")

i = int(input("Введите количество наименований на складе магазина: "))
products = []
quantity = []
unit = []
price = []
while len(products) != i:
    products.append(input("Наименование товара: "))
    quantity.append(input("Введите количество: "))
    unit.append(input("Единица измерения: "))
    price.append(input("Цена за единицу товара: "))
print(price, products, quantity, unit)
warehouse = {
    "Наименование": products,
    "Количество": quantity,
    "Единица измерения": unit,
    "Цена": price
}
print(warehouse)
analitic = (
    1, {"Наименование": products},
    2, {"Количество": quantity},
    3, {"Единица измерения": unit},
    3, {"Цена": price}
)
print(analitic)
