# #1
# n = int(input("Введіть число"))
# suma = 0
# count = 0
# average = 0
# for i in range(1, n+1):
#     if i % 3 == 0 or i % 5 == 0:
#         suma += i
#         count += 1
#         average = suma / count
#
# print(f'Сума {suma}, кількість {count}, середнє значення {round(average, 2)}')

#2
# n = int(input("Введіть число"))
# count = 0
# suma = 0
# max_digit = 0
# min_digit = 9
#
# if n == 0:
#     count = 1
#     suma = 0
#     max_digit = 0
#     min_digit = 0
# else:
#     while n > 0:
#         digit = n % 10
#         if digit > max_digit:
#             max_digit = digit
#         if digit < min_digit:
#             min_digit = digit
#         count += 1
#         suma += digit
#         n //= 10
# print(f'Сума {suma}, кількість цифр {count}, найбільша цифра {max_digit}, найменша цифра {min_digit}')

#3
# n = int(input("Введіть натуральне число"))
#
# for i in range(1, n+1):
#     correct = True
#     while i > 0:
#         digit = i % 10
#         if digit == 0:
#             correct = False
#             break
#         elif  i % digit != 0:
#             correct = False
#             break
#         i //= 10
#     if correct:
#         print(i)

#4
# width = int(input("Введіть ширину"))
# height = int(input("Введіть висоту"))
# contur = str(input("Введіть контур"))
# inside = str(input("Введіть середину"))
#
# if width < 3 or height < 3:
#     print('Введіть більше число')
#
# for row in range(height):
#     for col in range(width):
#         if row == 0 or row == height - 1:
#             print(contur,end=" ")
#         elif  col == 0 or col == width - 1  :
#             print(contur, end=" ")
#         else:
#             print(inside,end=" ")
#
#     print()
#
