import os

# #1
# try:
#     a = float(input("введіть число "))
#     b = float(input("введіть число "))
#     sing = input("введіть операцію ")
#     correct_operation = ["+", "-", "*", "/", "%", "**", "//"]
#     if sing not in correct_operation:
#         raise ValueError("Не відома опервація")
#     if sing == "+":
#         print(a + b)
#     elif sing == "-":
#         print(a - b)
#     elif sing == "*":
#         print(a * b)
#     elif sing == "/":
#         print(a / b)
#     elif sing == "%":
#         print(a % b)
#     elif sing == "**":
#         print(a ** b)
#     elif sing == "//":
#         print(a // b)
# except ZeroDivisionError:
#     print("не можна ділити на 0")
# except ValueError as error:
#     print(error)

#2
# def input_grade():
#     while True:
#         try:
#             try:
#                 grade = int(input("Введіть оцінку: "))
#             except ValueError:
#                 print("Потрібно ввести ціле число")
#                 continue
#             if grade < 1 or grade > 12:
#                 raise ValueError("Оцінка повинна бути від 1 до 12")
#             return grade
#         except ValueError as error:
#             print(error)
#
#
# grade = input_grade()
# print("Прийнято", grade)

#3
# students = ["Anna", "Masha", "Ivan", "Sophie", "Nika"]
# lines = {
#     'Math': 98,
#     'Physics': 80,
#     'IT': 70,
#     'Language': 64,
#
# }
# try:
#     chose = int(input("1-учень за індексом, 2-оцінка за назвою предмета: "))
#     if chose != 1 and chose != 2:
#         raise TypeError("Введіть число 1 або 2")
# except TypeError as error:
#     print(error)
# if chose == 1:
#     try:
#         index = int(input("Введіть індекс учня: "))
#         print(students[index])
#     except ValueError:
#         print("Введіть число")
#     except IndexError:
#         print("Учня з таким індексом немає")
# if chose == 2:
#     try:
#         key = input("Введіть назву предмету: ")
#         print(key, lines[key])
#     except KeyError:
#         print("Такого предмета немає")

#4
correct = []
skiped = 0
grades = {}
try:
    with open('students.txt', 'r', encoding="utf-8") as file:
        count = 0
        for line in file:
            count += 1
            try:
                name, score = line.strip().split(';')
            except ValueError:
                print(f'Рядок {count} пропущено: помилка з ";"')
                skiped += 1
                continue
            if name not in grades:
                grades[name] = []
            try:
                grades[name].append(int(score))
            except ValueError:
                print(f'Рядок {count} пропущено: бал не є цілим числом')
                skiped += 1
                continue

            try:
                if int(score) < 0 or int(score) > 100:
                    continue
            except ValueError as error:
                print(f'Рядок {count} пропущено: бал поза діапазоном')
                skiped += 1
                continue
except FileNotFoundError:
    print("File not found")

new_grades = sorted(grades.items(), )


with open('report.txt', 'w', encoding="utf-8") as file:
    for name, score in new_grades:
        print(f'{name};{score}', file=file)

print(f'Записів пропущено: {skiped}')
print(f'Правильних записів: {len(grades)}')
print("Створено report.txt")