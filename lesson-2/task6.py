#products = []
#while True:
   # all_products = input("Сколько всего наименований продукции? ")
   # if not all_products.isdigit():
   #     print("!!Введите число!!")
    #else:
    #    all_products = int(all_products)
     #   break
#print("Наименований", all_products)
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