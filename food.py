try:
    foodReceptions = int(input("Введите количество приёмов пищи: "))
except Exception:
    print("Произошла ошибка")
    quit()


totalCalories = 0
products = []

if foodReceptions > 0:
    for i in range(foodReceptions):
        print(f"\nПриём {i + 1}:")
        productName = input("Название продукта: ")
        productCalories = int(input("Количество калорий: "))
        products.append({"productName": productName, "productCalories": productCalories})
        totalCalories += productCalories

print(f"\nОбщее количество потребленных калорий за день: {totalCalories}\n")

seeProducts = input("Желаете увидеть список употребленных продуктов? (да/нет): ")

if seeProducts == "да":
    print("Список употребленных продуктов:")
    for i in products:
        print(f"- {i['productName']}: {i['productCalories']} калорий")
