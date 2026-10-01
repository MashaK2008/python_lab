#ітерація - одне виконання тіла циклу
#
#for i in range(1, 6, 2):
#    print(i)
#
#n = int(input())
#for i in range(1, n + 15, 1):
#    print(i)
#
#n = int(input())
#i = 1
#
#while i <= n:
#    print(i)
#    i += 1 # інкремент - збільшення на 1. декремент- зменшення на 1
#
#n = int(input())
#
#suma = 0
# for i in range(1, n+1):
#     suma += i
#print(f'Сума = {suma}')
#
#n = int(input())
#count = 0
#for i in range(1, n + 1):
#    if i % 2 == 0:
#        count += 1
#
#print(f'Парних чисел {count}')

#while True:
#    n = int(input('Введіть число або слово "0"'))
#      if n == "0":
#        break
#print(f'введено число {n}')

#for i in range(1, 11):
#    if i % 2 == 0:
#        continue
#    print(i)

#n = int(input('Введіть 4х значне число'))
#digit_last = n % 10
#digit_first = n % 100
#if digit_last == digit_first:
#    print("ok")
# n = int(input())
# while n > 0:
#     digit = n%10
#     print(f'остання цифра{digit}')
#     n //= 10

# n = int(input())
# max_digit = 0
# while n > 0:
#     digit = n % 10
#     if digit > max_digit:
#         max_digit = digit
#     n //= 10
# print(max_digit)

# for i in range(1, 6):
#     for j in range(1, 6):
#         print(i, j)

width = 6
height = 4
for row in range(height):
    for col in range(width):
        print("*",end=" ")
    print()

