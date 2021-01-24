products = []
while True:
    all_products = input("Сколько всего наименований продукции? ")
    if not all_products.isdigit():
        print("!!Введите число!!")
    else:
        all_products = int(all_products)
        break
print("Наименований", all_products)
