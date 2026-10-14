import os
# name= input("enter your name: ")

# print("Створення файлу")
#
with open('Hello.txt', 'w', encoding='utf-8') as file:
    file.write('Я точно зроблю ман!\n')
#
# r - режим читання, файл вже має шснуватти
# w - запис, якщо файл вже існує, то його вміст стирається та перезаписується
# a - додає контет в кінець, якщо файл не створено він сворить новий файл
# x - створення нового файлу, але якщо такий файл існує то буде помилка

if not os.path.exists('text.txt'):
    with open('text.txt', 'w', encoding="utf-8") as file:
        file.write("Python - популярна мова програмування. \n")
        file.write("Python використовується для роботи з даними. \n")
        file.write("Файли дозволяють зберігати інформацію. \n")
        file.write("Python вимагає практики. \n")
        file.write("Сьогодні ми працюємо з текстовими файлами. \n")

if not os.path.exists('numbers.txt'):
    with open('numbers.txt', 'w', encoding="utf-8") as file:
        file.write("12\n8\n25\n4\n16\n")

if not os.path.exists('students.txt'):
    with open('students.txt', 'w', encoding="utf-8") as file:
        file.write("Ivanenko Anna;91\n")
        file.write("Leshchenko Ivan;76 \n")
        file.write("Komarova Sophie;97 \n")
        file.write("Bondarenko Illya;84 \n")

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


with open('text.txt', 'r', encoding="utf-8") as file:
    text = file.read()
print(text)
# with - автоматично закриває після завершення його роботи
#file - просто імя змінної
#text.txt - шлях файлв який ми відкриваємо
with open('log.txt', 'w', encoding="utf-8") as file:
    file.write("Перший запуск\n")
with open('log.txt', 'w', encoding="utf-8") as file:
    file.write("Другий запуск, перший видалено\n")
with open('log.txt', 'a', encoding="utf-8") as file:
    file.write("Новий зарис додаємо у кінець\n")
with open('log.txt', 'r', encoding="utf-8") as file:
    print(file.read())

#способи читання
with open('text.txt', 'r', encoding="utf-8") as file:
    text = file.read()
print(f'read -> {type(text)}, count -> {len(text)}')

with open('text.txt', 'r', encoding="utf-8") as file:
    line1 = file.readline()#наступний рядок
    other_lines = file.readlines()#створюється список з усіх рядків які ще не булт до цього прочитані
    line2 = file.readline() #line1=line2
print(line1)
print(line2)
print(other_lines)

with open('text.txt', 'r', encoding="utf-8") as file:
    lines = file.readlines()
print(other_lines)
print(other_lines[0] if lines else 'файл порожній')

#перебір файлу
with open('text.txt', 'r', encoding="utf-8") as file:
    for number, line in enumerate(file, start=1):
        clean_line = line.strip()
        print(f'number -> {number}, line -> {clean_line}')

#розпакування
line = "Ivanenko Anna;91\n"
clean_line = line.strip()
name, score = line.split(';')
print(f'name -> {name}, score -> {score}')

numbers =[]
with open('numbers.txt', 'r', encoding="utf-8") as file:
    for line in file:
        numbers.append(int(line.strip()))
print(numbers)

students = []
with open('students.txt', 'r', encoding="utf-8") as file:
    for line in file:
        name, score = line.strip().split(';')
        students.append([name, int(score)])
print(students)

#CSv
grades = []
with open('grades.csv', 'r', encoding="utf-8") as file:
    for line in file:
        name, subject, score = line.strip().split(';')
        grades.append([name,subject, int(score)])


