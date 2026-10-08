#1
from operator import truediv
from shlex import split


# pi = 3.14159
# def rectangle_area(width, height):
#     return width * height
# def triangle_area(side, height):
#     return 0,5*(side * height)
# def circle_area(radius):
#     return pi*(radius**2)
#
# def main():
#     print("Площу якої фігури хочете порахувати: 1. Трикутник 2. Прямокутник 3. Коло")
#     choice =int(input("Введіть цифру: "))
#     if choice == 1:
#         side = float(input("введіть сторону трикутника: "))
#         height = float(input("введіть висоту трикутника: "))
#         print("Площа трикутника: ", triangle_area(side, height))
#
#     elif choice == 2:
#         width = float(input("введіть ширину прямокутника: "))
#         height = float(input("введіть висоту прямокутника: "))
#         print("Площа прямокутника: ", rectangle_area(width, height))
#
#     elif choice == 3:
#         radius = float(input("введіть радіус кола: "))
#         print("Площа кола: ", circle_area(radius))
#
# main()

#2

# def is_prime(n):
#     if n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0 or n == 1 :
#         return "ні"
#     else :
#         return "так"
# def divisors(n):
#     return [i for i in range(1, n + 1) if n % i == 0]
# def digit_sum(n):
#     sum = 0
#     num = n
#     while num > 0:
#         digit = num % 10
#         sum += digit
#         num //= 10
#     return sum
# def main():
#     n = int(input("введіть число"))
#     print(f'просте число: {is_prime(n)}')
#     print(f'дільники: {divisors(n)}')
#     print(f'сума цифр: {digit_sum(n)}')
# main()

#3

# def average(grades):
#     return sum(grades)/len(grades)
# def minimum(grades):
#     return min(grades)
# def maximum(grades):
#     return max(grades)
# def count_above(grades, value):
#     more = 0
#     for grade in grades:
#         if grade > value:
#             more += 1
#     return more
# def main():
#     grades_input = input("введіть оцінки: ").split()
#     grades = []
#     for grade in grades_input:
#         grades.append(int(grade))
#     print(average(grades))
#     print(minimum(grades))
#     print(maximum(grades))
#     print(count_above(grades, int(input("ВВедіть мінімальну оцінку: "))))
# main()

#4

def minimum_length(password):
    if len(password) >= 8:
        return True
    else:
        return False
def number(password):
    for char in password:
        if char.isdigit():
            return True
    return False
def high(password):
    for char in password:
        if char.isalpha():
            if char == char.upper():
                return True
    return False
def low(password):
    for char in password:
        if char.isalpha():
            if char == char.lower():
                return True
    return False
def special(password):
    for char in password:
        if password.isalnum():
            return False
    return True

def validate_password(password):
    mistake = []
    if minimum_length(password) == False:
        mistake.append("Мінімальна довжина 8 символів")
    if number(password) == False:
        mistake.append("Має буди хоча б 1 цифра")
    if high(password) == False:
        mistake.append("Має бути хоча б 1 велика літера")
    if low(password) == False:
        mistake.append("Має бути хоча б 1 мала літера")
    if special(password) == False:
        mistake.append("Має бути хоча б 1 спеціальний символ")
    return mistake
def main():
    password = input("Введіть пароль")
    if len(validate_password(password)) == 0:
        print("Пароль вірний")
    else:
        print("Пароль не відповідає вимогам")
        for i in validate_password(password):
            print(f'Не виконано {i}')

main()











