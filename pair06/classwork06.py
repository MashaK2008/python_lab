from math import sqrt
from math import *
import statistics as st
import random
from datetime import datetime, date
import demo
from tkinter import *


# a = 81
# print(sqrt(a))
#
# grades = [10, 7, 9, 2, 11]
# print(f'Середній бал: {st.mean(grades)}')
# print(f'mode: {st.mode(grades)}')
# print(f'median: {st.median(grades)}')
#
#
# radius = 5
# print(f'площа круга: {round((pi * pow(radius, 2)), 2)}')
#
# b = 2.4343453
# print(ceil(b))
# print(floor(b))
#
# balls = 25
# items = 6
#
# print(f'Повністю заповнені коробки: {floor(balls / items)}')
# print(f'Коробок потрібно всього: {ceil(balls / items )}')
#
# numbers = []
# for i in range(10):
#     numbers.append(random.randint(1, 100))
# print(numbers)
#
# names = ['Ivan', 'Matvey', 'Maria']
# print(random.choice(names))
#
# print(f'Сьогодні: {datetime.today()}')
# print(f'Зараз: {datetime.now()}')
#
# year = 2026
# day = 31
# month = 12
#
# user_date = datetime.today()
#
# print(demo.square(5))
# grades2 = [10, 7, 9, 2, 11, 2]
# print(demo.average(grades2))

def text():
    text = "Welcome to the game"
    label2['text'] = text
def clear(event):
    label2['text'] = " "

window = Tk()
window.title("My first program")
window.geometry("500x500")
window.resizable(width=False, height=False)
# window.configure(background="white")
window["bg"] = "#E32636"
label = Label(window, text = "my first program", bg ="#E32636", font = ("Arial", 25))
# label.pack()
# label.place(x=100, y=200)
label.grid(row=0, column=0, columnspan=2)
btn1 = Button(window, text="OK", font = ("Arial", 20), width= 8, activebackground="#FFBF00", command = text)
btn1.grid(row=1, column=0, pady = 20, padx = 10)
bnt2 = Button(window, text="Cancel", font = ("Arial", 20), width= 8, activebackground="#FFBF00")
bnt2.grid(row=1, column=1, pady = 20, padx = 10)
bnt2.bind("<Button-1>", clear)

label2 = Label(window, text='', bg ="#E32636", font = ("Arial", 25))
label2.grid(row=2, column=0, columnspan=2)





window.mainloop()