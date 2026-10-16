# book = {
#     'title': "Кобзар",
#     'author': "Тарас Шевченко",
#     'copies': 15
#
# }

# class Book:
#     def __init__(self, title, author, copies):
#         self.title = title #self Вказуємо що саме з цим елементом ми працюємо
#         self.author = author
#         self.copies = copies
#     def available(self):
#         return self.copies > 0
#
# book1= Book('Кобзар', 'Тарас Шевчнко', 15)
#
# print(book1.title, book1.author, book1.copies)
# print(book1.available())

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def area(self):
#         return self.width * self.height
#     def perimeter(self):
#         return self.width * 2 + self.height * 2
#     def info(self):
#         print(f'Rectangle width: {self.width}, height: {self.height}')
#         print(f'Perimeter: {self.perimeter()}')
#         print(f'Area: {self.area()}')
#
# rectangle = Rectangle(4, 5)
# rectangle.info()

# class Counter:
#     def __init__(self):
#         self.value = 0
#
#     def increment(self):
#         self.value += 1
#
# counter1 = Counter()
# counter2 = Counter()
# print(f'було {counter1.value, counter2.value}')
# counter1.increment()
# counter1.increment()
# print(f'стало {counter1.value, counter2.value}')

# class Book:
#     def __init__(self, title, copies):
#         self.title = title
#         self.copies = copies
#
#     def give_one(self):
#         if self.copies > 0:
#             self.copies -= 1
#             print(f"Видано книгу {self.title}")
#         else:
#             print(f"Немвє доступних примірників {self.title}")
# book = Book("Кобзар", 1)
# book.give_one()
# book.give_one()
# print(f'Залишилось: {book.copies}')

# class Student:
#     def __init__(self, name, grades):
#         self.name = name
#         self.grades = grades
#     def add_grade(self, grade):
#         if grade >=1 and grade <=12:
#             self.grades.append(grade)
#         else:
#             print('Grade must be between 1 and 12')
#     def average_grade(self):
#         if len(self.grades)==0:
#             return 0
#         else:
#             return sum(self.grades)/len(self.grades)
#     def info(self):
#         print(f'Name: {self.name}, Grades: {self.grades}')
#     def __str__(self):
#         return f'Student name: {self.name}, Grades: {self.grades}, Average: {self.average_grade()}'
# # student1 = Student("Ivan")
# student2 = Student("Anna")
# student1.add_grade(12)
# student1.add_grade(10)
# student2.add_grade(13)
# student1.info()
# student2.info()
# print(f'Ivan: {student1.grades}, Anna: {student2.grades}')
# print(f'Student average: {student1.average_grade()}')
# print(f'Student average: {student2.average_grade()}')
#
# students = [
#     Student('Anna', [1, 2, 3]),
#     Student("Ivan", [12, 10, 11])
#
# ]
# print(f'Students: {len(students)}')
# for student in students:
#     print(f'Student: {student.name}, Grades: {student.grades}')

class Product:
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count
    def total_price(self):
        return self.price * self.count

mouse = Product("Mouse", 1500, 10)
keyboard = Product("Keyboard", 2000, 4)
print(mouse.total_price())
print(keyboard.total_price())