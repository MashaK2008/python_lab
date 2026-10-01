# #1
# text = input("Введи речення: ").strip().lower()
#
# simvol = len(text)
# print('Кількість символів: ', simvol)
#
# numbers = '1234567890'
# number_count = 0
# for num in text:
#     if num in numbers:
#         number_count += 1
# print('Кількість чисел: ', number_count)
#
# letters_count = 0
# for char in text:
#     if char != ' '  and char != numbers:
#         letters_count += 1
# print('Кількість букв: ',letters_count)
#
# golosni = 'аеєиіїоуюя'
# counter_golosni = 0
# for i in text:
#     if i in golosni:
#         counter_golosni += 1
# print('Кількість голосних:', counter_golosni)
#
# probil_counter = 0
# for i in text:
#     if i == ' ':
#         probil_counter += 1
# print('Кількість пробілів:', probil_counter)
#
# words = text.split()
# words_count = len(words)
# print('Кідбкість слів: ', words_count)

#2

# pib = input("Веддіть прізвище, ім'я, по батькові ").lower().title().strip().split()
# if len(pib) != 3:
#     print("напишіть правильно!!!")
# name = pib[1]
# last_name = pib[0]
# pobatcovi = pib[2]
# print(f'{last_name} {name[0]}. {pobatcovi[0]}.')

#3

# string1 = input("Введіть можливу анограму: ").strip().lower().replace(" ","")
# string2 = input("Введіть можливу анограму: ").strip().lower().replace(" ","")
# long = len(string1)
# long1 = 0
# for i in string1:
#     for j in string2:
#         while i == j:
#             if i == j:
#                 long1 = long1 + 1
#             else:
#                 break
# if long == long1:
#     print("анограма")
# else:
#     print('не анограма')

#4

string = input('Enter a string: ').lower().split()
longest_word = string[0]
shortest_word = string[0]
unique = 0
for word in string:
    if len(word) > len(longest_word):
        longest_word = word

    if len(word) < len(shortest_word):
        shortest_word = word
    if string.count(word) == 1:
        unique += 1
print(longest_word, shortest_word, unique)
zamina = input('Enter a number: ')
zamina_final = input('Enter a number: ')
new_string = " ".join(string)
new_string = new_string.replace(zamina, zamina_final)
print(new_string)


