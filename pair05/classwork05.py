# def say_hello():
#     print("Hello World")
# say_hello()

# def say_hello(name): #name - параметр
#     print(f'Hello {name}!!')
#
# say_hello("Masha")#masha - аргумент - значення під час виклику
# say_hello("Tanya")

# def rectangle_area(width, height = 10):
#     return width * height
#
# width = int(input("введіть ширину прямокутника: "))
# height = int(input("введіть висоту прямокутника: "))
#
# s = rectangle_area(width, height)
# print(f"Площа дорівнює {s} см2")

# def hello_world(name, message = 'Hello world'):
#     print(f'Hello {name}, your message is {message}!!!')
#
# hello_world('Maha')

# def price_with_discount(price, discount = 0):
#     return price - price * discount / 100
#
# print(price_with_discount(1000))

# def min_max(numbers):
#     return min(numbers), max(numbers)
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# min_, max_ = min_max(numbers)

# def is_even(num):
#     """"Повертає True якщо парне - інакше false"""
#     return num % 2 == 0
#
# print(is_even(3))
# print(is_even.__doc__)

# def rectngle_area(width, height):
#     return width * height
#
# def main():
#     width = float(input("width: "))
#     height = float(input("height: "))
#
#     print(f'ширина, {width}')
#     print(f'висота, {height}')
#     result = rectngle_area(width, height)
#     print(f'Площа прямокутника: {result}')
#
# main()