
from math import*
from random import*
import statistics as st


def generate_grades(count):
    grades = []
    for i in range(count+1):
        grades.append(randint(1, 12))
    return grades

def average_grades(grades):
    average = round(st.mean(grades), 2)
    return average

def get_level(average):
    if average >= 10:
        return "високий"
    elif average >= 7:
        return "достатній"
    elif average >= 4:
        return "середній"
    else:
        return "початковий"
