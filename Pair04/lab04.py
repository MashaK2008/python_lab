# #1
# numbers = [12, 3, 4, 14, -12, 5, 10, 16, -4]
# plus =[]
# minus =[]
# parni = []
# na3 = []
# for number in numbers:
#     if number > 0:
#         plus.append(number)
#     else :
#         minus.append(number)
#     if number % 2 == 0:
#         parni.append(number)
#     if number % 3 == 0:
#         na3.append(number)
# print("Додатні: ", plus)
# print("Від'ємні: ", minus)
# print("Парні: ", parni)
# print("Кратні 3: ", na3)
# print(f"Min: {min(numbers)}, Max: {max(numbers)}, Sum: {sum(numbers)}, Average: {round(sum(numbers) / len(numbers), 2)}")

#2
# group1 = {'Anna', 'Ivan', 'Olha'}
# group2 = {'Ivan', 'Maxim', 'Olha'}
# group3 = group1 & group2
# group4 = group1 | group2
# group5 = group1 - group2
# group6 = group2 - group1
# print("Спільні: ", group3)
# print("Тільки group1: ", group5)
# print("Тільки group2: ", group6)
# print("Усі: ", group4)

#3

# price = {
#     'milk': 48,
#     'coffe': 80,
#     'tea': 75,
#     'juice': 30,
#     'coca-cola': 40
# }
#
# for key, value in price.items():
#     print(f"{key}: {value}")
#
# novy_tovar = input("Введіть назву нового товару ")
# novy_price = int(input("Введіть ціну нового товару "))
# price[novy_tovar] = novy_price
# for key, value in price.items():
#     print(f"{key}: {value}")
#
# zamina_tovar = input("Введіть назву товара якому треба замінити ціну ")
# zamina_price = int(input("На яку ціну потрбно замінити "))
# price[zamina_tovar] = zamina_price
# for key, value in price.items():
#     print(f"{key}: {value}")
#
# nazva = input("Введіть назву шуканого товару ")
# print(price.get(nazva), "такого немає")
#
#
# minimum = int(input("Мінімальна ціна "))
# maximum = int(input("Максимальна ціна "))
# for name, price in price.items():
#     if price > minimum and price <= maximum:
#         print(f"{name}: {price}грн")

#4
group_info = ('10-IT', '2026/2027')
zurnal = {
    'Anna': [10, 11, 12, 9, 10],
    'Ivan': [8, 9, 10, 11, 9]
}

for k, v in zurnal.items():
    if len(v) > 5:
        print('максимум 5 оцінок')
        zurnal[k] = v[:5]

novy_uchen = input("Введіть ім'я ")
novy_grades = input('Введіть оцінки учня ').split()
grades = []
for i in novy_grades:
    grades.append(int(i))
zurnal[novy_uchen] = grades

if len(v) > 5:
    print('максимум 5 оцінок')
    grades = grades[:5]
for g in grades:
    if g < 1 or g > 12:
        print('Оцінка від 1 до 12')
        novy_grades = input('Введіть оцінки учня ')
        grades = []
        for i in novy_grades:
            grades.append(int(i))

print(group_info)
for key, value in zurnal.items():
    print(f"{key}: {value}")

for key, value in zurnal.items():
    average = sum(value) / len(value)
    print(f"Середій бал {key}: {round(average, 2)}")

the_best = 0
for key, value in zurnal.items():
    if average > the_best:
        the_best = average
print(the_best)

