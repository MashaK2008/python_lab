# name = "Masha"
# city = "Kyiv"
# message = "hello world"
#
# print(len(message))#повертає кількість символів
# print(name[0])
# print(name[-1])#-1 останній елемент
# print(message[len(message)-1])
# print(city[10])

# text = "hello world"
# if len(text) > 0:
#     print(text[0])
# else :
#     print("рядок порожній")
# print(text[:2])
# print(text[2:])
# print(text[2:5])
# print(text[::2])#зріз через 1 символ
# print(text[::-1])#пише задом нареоед
# строки незмінні

# text = "hello world"
# print(text.upper()) #пише все зв великої
# print(text.lower()) #пише все малим
# print(text.capitalize())#Записує з великої літери на початку строки
# print(text.title()) #пише кожне слово з великої

# text = "      Python     programming        "
# print(text.lstrip())#видаляє пробіли ліворуч рядка
# print(text.rstrip())#видаляє пробіли праворуч рядка
# print(text.strip()) #видаляє і справа і щліва але не в цунтрі

# login = "admin"
# user_login = input("Enter your login : ")
# if user_login.strip().lower() == login:
#     print("Login Successful")

# text = "Python"
# for i in text:
#     print(i)
#
# password = "123qwerty123"
# digits = 0
# letters = 0
# for i in password:
#     if i.isdigit(): #метод який переіояє чи складається строка з цифр
#         digits += 1
#     if i.isalpha():
#         letters += 1
# print (f'Цифр: {digits} літер: {letters}')
#
# print (password.isalpha())#метод який перевіряє чи складажться строка тільки з літер
# print (password.isalnum())#метод який перевіряє чи складається строка тільки з літер або цифр
# print (password.isdigit())#метод який переіояє чи складається строка з цифр
#

# text = input("Введи речення: ").strip().lower()
# golosni = 'аеєиіїоуюя'
# counter_golosni = 0
#
# for i in text:
#     if i in golosni:
#         counter_golosni += 1
# print(counter_golosni)

# text = "привіт світ"
# words = text.split()#перетворює в список по пробілу
# print(words)
#
# text_new = ' '.join(words)#робить із списка рядок
# print(text_new)

# text = "Python is easy to learn"
# new_text = text.replace("Python", "JavaScript")#замінює з вже існуючої строки
# print(new_text)

# word = 'Дід '
# word_norm = word.strip().lower()
# if word_norm == word_norm[::-1]
#     print('Полідром')
# else:
#     print('Не полідром')

# text = 'hello world'
# print(text.find('o'))
# print(text.count('l'))

email = 'teacher.ivan.komarov@gmail.com'
if email.lower().endswith('@gmail.com'): #.startswith
    print('у тебе гуглівська почта')