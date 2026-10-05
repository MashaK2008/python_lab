# #list - список - впорядкована зміна колкція
# grades = [10, 8, 9]
# numbers = []
# numbers_new = list()
#
# grades[1] = 12
# print(grades)
#
# numbers.append(10)
# numbers.append([11, 4])
# numbers.insert(1, [5, 6] )#- додає емеиент за індексрм
# numbers.extend([7, 8, 9, 7, 8, 5, 8]) # - додавання декількох елементів
# numbers.remove(7)
# numbers.pop(1) # видалення за індексом
# #del numbers[1]
# #numbers.clear() #щчищає список
# print(numbers.count(8))
# print(numbers.index(8))
# print(8 in numbers)
# # len()
# # min()
# # max()
# # sum()
#
# print(numbers)

# numbers = [1, 4, 6, 8, 3]
# numbers.sort(reverse=True)
# print(numbers)
#
# new_numbers = sorted(numbers)
# new_numbers.reverse()
# print(new_numbers)
#
# for number in numbers:
#     print(number)

# numbers = [1, -9, -4, 0, 34, 5, -3]
# positive = []
# for number in numbers:
#     if number > 0:
#         positive.append(number)
# print(positive)


#tuple - картежі впорядкована незміна колекція
# point = (-10, 12)
# rgb = (255, 0, 0)
# data = ()
# student = "Masha", "Kardash"
# print(student)
# a = (10,)
# point = point + (30, )
# print(point)
# print(point + a)
# point = point[:1] + point[2:]
# print(point)
# point = (-12, 6)
# x, y = point
# print(x)
# print(y)


#set - множини не має дублікатів не має індексного допису на порядок елеменьів не звертаємо увагу, можна додавати й видаляти елементи
# subjects = {"Python", "HTML", "CSS", "JavaScript"}
# data = {}
# print(type(data))
# subjects.add("C++")
# subjects.update(["Java", "Python"])
# print(subjects)
# subjects.remove("Java")
# subjects.discard("C#")
# if "Python" in subjects:
#     print("Python")
# name = ["Ivan", "Oleg", "Olha", "Ivan", "Maria", "Maria"]
# unique_names = set(name)
# print(unique_names)
#
# group1 = {"Ivan", "Oleg", "Olha"}
# group2 = {"Ivan", "Maria", "Ann"}
#
# group3 = group1 & group2#обєднання
# group4 = group1 | group2#переьтн
# group5 = group1 - group2#які є в 1 але відсутні в 2
# print(group3)
# print(group4)
# print(group5)


#dict - словники
# student = {
#     "name": "Masha",
#     "grade": 11
# }
# student2 = {}
# student3 = dict()
# print(student["name"])
# student["age"] = 18
# print(student)
# student["age"] = 19
# print(student)
# student_update = student.pop("age")
# print(student_update)
# popitem = student.popitem()

# student = {
#     "name": "Masha",
#     "grade": 11
# }
#
# print(student.get("age", "Такого немає(("))
# if "grade" in student:
#     print(student.get("grade"))
#
# if "Masha" in student.values():
#     print(student.get("name"))
#
# if "Masha" in student.keys():
#     print(student.get("name"))
#
# print(student.items())
#
# for key, value in student.items():
#     print(key)
#     print(value)

price = {
    'apple': 50,
    'banana': 70,
    'kiwi': 70,
    'mango': 150,
    'orange': 100
}
print('Усі товари: ', price)
for key, value in price.items():
    print(f"{key}: {value}грн")
print("від 50 до 100 грн")
for name, price in price.items():
    if price > 50 and price <= 100:
        print(f"{name}: {price}грн")
#Колекція структура данних яка дозволяє зберігати струкктури данних