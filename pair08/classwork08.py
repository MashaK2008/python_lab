# if 5 > 2
#     print("YES")

# n = int("Hello"))

# try:
#     age = int(input("Enter your age: "))
#     print("Your age " + str(age))
# except ValueError:
#     print("please enter a valid age")

# try:
#     a = float(input("a = "))
#     b = float(input("b = "))
#     result = a / b
#     print(result)
# except ValueError:
#     print("Введено не число")
# except ZeroDivisionError:
#     print("не можна дділити на нуль")

# try:
#     number = int(input("Enter a number: "))
# except ValueError:
#     print("Enter a NUMBER")
# else:
#     print("Квадрат від числа: ", number ** 2)

# try:
#     number = int(input("Please enter a number: "))
#     print(100/ number)
# except ValueError:
#     print("Please enter a number")
# except ZeroDivisionError:
#     print("Please enter not 0")
# finally:
#     print("Goodbye")

#
# while True:
#     try:
#         grade = int(input("Введіть оцінку від 1 до 12"))
#         if grade < 1 or grade > 12:
#             raise ValueError("Grade between 1 and 12")
#         print(f'your grade is {grade}')
#         break
#     except ValueError as error:
#         print(f'error:{error}')

# def int_input(message):
#     while True:
#         try:
#             return int(input(message))
#         except ValueError:
#             print("Please enter an integer")
#
# count = int_input("Please enter a number")
# print(f'Кількість: {count}')

# def input_grade():
#     while True:
#         try:
#             grade = int(input("Enter your grade: "))
#             if grade < 1 or grade > 12:
#                 raise ValueError("Grade must be between 1 and 12")
#             return grade
#         except ValueError as error:
#             print( error)
#
# grade = input_grade()
# print("Прийнято", grade)

#students = ["Anna", "Ivan", "Sophie"]
# try:
#     index = int(input("Please enter a number: "))
#     print(students[index])
# except ValueError:
#     print("Please enter a number")
# except IndexError:
#     print("елемента з таким індексом не існує")


# price = {
#     "apple": 100,
#     "banana": 200,
#     "mango": 300,
# }
# product = input("Enter product name: ")
# # try:
# #     print(f'Ціна: {price[product]}')
# # except KeyError:
# #     print("Такого товару немає")
#
# price = price.get(product, "немає у наявності")
# print(price)

# try:
#     with open("dara.txt", "r", encoding="utf-8") as file:
#         data = file.read()
#         print(data)
# except FileNotFoundError:
#     print("File not found")

# line = "Anna;600"
#
# parts = line.strip().split(";")
# if len(parts) != 2:
#     print("Error")
# else:
#     name = parts[0]
#     grade = parts[1]
#     try:
#         score = int(grade)
#         if score < 0 or score > 100:
#             raise ValueError("SCORE MUST BE between 0 and 100")
#     except ValueError as error:
#         print(error)
#     else:
#         print(f"Запис правильний {name}: {score}")

lines = [
    'Anna;90'
    'Ivan;hello'
    'Matvey;99'

]
for line_number, line in enumerate(lines, start=1):
    parts = line.strip().split(';')
    if len(parts) != 2:
        print(f'Рядок №{line_number}  пропущено через неправильний формат\n{line}')
        continue

    name = parts[0]
    grade = parts[1]
    try:
        grade = int(grade)
    except ValueError:
        print(f'Рядок №{line_number}, пропущено: бал не є числом')
        continue
    print("Правильний запис", name, grade)