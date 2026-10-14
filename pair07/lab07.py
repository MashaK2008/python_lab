import os
#1
# if not os.path.exists('text.txt'):
#     with open('text.txt', 'w', encoding="utf-8") as file:
#         file.write("Python - популярна мова програмування.\n")
#         file.write("Python використовується для роботи з даними.\n")
#         file.write("Файли дозволяють зберігати інформацію.\n")
#         file.write("Python вимагає практики.\n")
#         file.write("Сьогодні ми працюємо з текстовими файлами.\n")
# lines = 0
# words = 0
# symbols = 0
# longest = ''
# with open('text.txt', 'r', encoding="utf-8") as file:
#     for line in file:
#         new_line = line.strip("\n")
#         lines += 1
#         if len(new_line) > len(longest):
#             longest = new_line
#             number = lines
#         symbols += len(new_line.strip())
#         for word in new_line.split():
#             new_word = word.strip('.')
#             if new_word.isalpha():
#                 words += 1
#
# print("Рядків: ", lines)
# print("Слів: ", words)
# print("Символів: ", symbols)
# print(f'Найдовший рядок: №{number}, {len(longest)}')
# print("Текст: ", longest)

#2
# if not os.path.exists('text.txt'):
#     with open('text.txt', 'w', encoding="utf-8") as file:
#         file.write("Python - популярна мова програмування.\n")
#         file.write("Python використовується для роботи з даними.\n")
#         file.write("Файли дозволяють зберігати інформацію.\n")
#         file.write("Python вимагає практики.\n")
#         file.write("Сьогодні ми працюємо з текстовими файлами.\n")
# search = input("Введіть слово яке потрібно знайти: ").lower()
# lines = 0
# with open('text.txt', 'r', encoding="utf-8") as file:
#     for line in file:
#         lines += 1
#         new_line = line.lower()
#         if search in new_line:
#             number = lines
#             print(f'{number}: {line}')

#3
# if not os.path.exists('students.txt'):
#     with open('students.txt', 'w', encoding="utf-8") as file:
#         file.write("Ivanenko Anna;91\n")
#         file.write("Leshchenko Ivan;76\n")
#         file.write("Komarova Sophie;97\n")
#         file.write("Bondarenko Illya;84\n")
# students = []
# with open('students.txt', 'r', encoding="utf-8") as file:
#      for line in file:
#         new_line = line.strip("\n").split(";")
#         if int(new_line[1]) > 80:
#             students.append(new_line,)
# students.sort(key=lambda student: student[1], reverse = True)
#
# with open('result.txt', 'w', encoding="utf-8") as file:
#     for name, score in students:
#         print(f'{name};{score}')


#4

if not os.path.exists('grades.csv'):
    with open('grades.csv', 'w', encoding="utf-8") as file:
        file.write("Anna;Python;11\n")
        file.write("Anna;Math;10\n")
        file.write("Ivan;Python;6 \n")
        file.write("Ivan;Math;5 \n")
        file.write("Sophie;Python;11 \n")
        file.write("Sophie;Math;12 \n")
        file.write("Illya;Python;9 \n")
        file.write("Illya;Math;8 \n")
grades = {}
with open('grades.csv', 'r', encoding="utf-8") as file:
    for line in file:
        name, subject, score = line.strip().split(';')
        if name not in grades:
            grades[name] = []
        grades[name].append(int(score))
highest = 0
best = ''
for name, score in grades.items():
    avg = sum(score)/len(score)
    if avg > highest:
        highest = avg
        best = name

with open('report.txt', 'w', encoding="utf-8") as file:
    for name, score in grades.items():
        avg = sum(score) / len(score)
        print(f'{name}, оцінок: {len(score)}, середній: {avg}')
    print(f'Найкращий результат: {best}, {highest}')


