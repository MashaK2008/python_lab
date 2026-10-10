import statistics
from math import*
from random import*
import statistics as st
from datetime import datetime, date
import tkinter as tk
import student_utils

#1
# radius = float(input("введіть радіус: "))
# cateti = input("Введіть катети ").split()
# items = float(input("введіть кількість предметів: "))
# in_package = float(input("введіть скільки вміщає упаковка: "))
# print(f'Площа круга: {round(pi*radius**2, 2)}')
# print(f'Гіпотенуза: {sqrt(float(cateti[0])**2 + float(cateti[1])**2)}')
# print(f'Потрібно упаковок: {ceil(items / in_package)}')

#2

# number = int(input("Введіть кількість оцінок: "))
# if number < 0:
#     print("Кількість має бути додатня")
#     number = int(input("Введіть кількість оцінок: "))
# grades = []
# for i in range(number):
#     grades.append(randint(1, 12))
# print(grades)
# print(f'Min: {min(grades)}')
# print(f'Max: {max(grades)}')
# print(f'Середнє: {round(statistics.mean(grades), 2)}')
# print(f'Медіана: {statistics.median(grades)}')
# more = 0
# for i in grades:
#     if i >= 10:
#         more += 1
# print(f'Оцінок 10-12: {more}')

#3
# person_input = input("Введіть дату(рік, місяць, день): ").split()
# person_date = date(int(person_input[0]), int(person_input[1]), int(person_input[2]))
# date_now = date.today()
# difference = person_date - date_now
# if difference.days > 0:
#     print(f'До події залишилося: {int(difference.days)} днів')
# elif difference.days < 0:
#     print(f'Подія була: {int(difference.days)*(-1)} днів тому')
# else:
#     print(f'Подія сьогодні')

#4
students_list = ["Anna", "Ivan", "Olha"]
students = ''.join(students_list, )
print(f'Учні: {students}')
def generate_report():
    value = entry_count.get().strip()
    if not value.isdecimal():
        Text.delete(1.0, tk.END)
        Text.insert(tk.END, "Введіть ціле число від 1 до 20")
        return


    count = int(value)
    if count < 1 or count > 20:
        Text.delete(1.0, tk.END)
        Text.insert(tk.END, "Введіть ціле число від 1 до 20")
        return



    report = ''
    for student in students_list:
        grades = student_utils.generate_grades(count)
        avg = student_utils.average_grades(grades)
        level = student_utils.get_level(avg)
        print(f'{student}: {grades}, {avg}, {level} ')
        report += f'{student}: {grades}, {avg}, {level} '
        Text.delete(1.0, tk.END)
        Text.insert(tk.END, report)


window = tk.Tk()
window.title("Статистика учнів")
window.geometry("600x700")
label_info = tk.Label(window, text = "Введіть кількість оцінок(1-20):", font = ("Arial", 20))
label_info.grid(row=0, column=0, columnspan=2)
entry_count = tk.Entry(window, font = ("Arial", 20))
entry_count.grid(row=1, column=0, pady = 20, padx = 10)
btn1 = tk.Button(window, text="Сформувати звіт", command=generate_report)
btn1.grid(row=1, column=1, pady = 20, padx = 10)
Text = tk.Text(window,  font = ("Arial", 20), width= 20)
Text.grid(row=2, column=0, pady = 20, padx = 10)
window.mainloop()





