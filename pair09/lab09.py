#1

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def area(self):
#         return self.width * self.height
#     def perimeter(self):
#         return 2*(self.width + self.height)
#     def info(self):
#         print(f'{self.width} x {self.height}, периметр: {self.perimeter()}, площа: {self.area()}')
#
# rectangle1 = Rectangle(4, 5)
# rectangle2 = Rectangle(6, 7)
# rectangle1.info()
# rectangle2.info()

#2

# class Student:
#     def __init__(self, name, grades):
#         self.name = name
#         self.grades = grades
#     def add_grade(self, grade):
#         if grade >= 1 and grade <= 12:
#             self.grades.append(grade)
#         else:
#             print(f'Оцінка {grade} не додається ')
#
#
#     def average_grade(self):
#         if len(self.grades)==0:
#             return 0
#         else:
#             return round(sum(self.grades)/len(self.grades), 2)
#     def __str__(self):
#         return f'{self.name}: {self.grades}, середній: {self.average_grade()}'
#
# student1 = Student('Ivan Petrenko', [])
# student1.add_grade(15)
# student1.add_grade(9)
# student1.add_grade(7)
# student1.add_grade(9)
# info = student1.__str__()
# print(info)


#3

# class Student:
#     def __init__(self, name, grades):
#         self.name = name
#         self.grades = grades
#     def add_grade(self, grade):
#         if grade >= 1 and grade <= 12:
#             self.grades.append(grade)
#         else:
#             print(f'Оцінка {grade} не додається ')
#
#
#     def average_grade(self):
#         if len(self.grades)==0:
#             return 0
#         else:
#             return round(sum(self.grades)/len(self.grades), 2)
#     def __str__(self):
#         return f'{self.name} - {self.average_grade()}'
#
# students = [
#     Student('Anna', [1, 2, 3]),
#     Student("Ivan", [12, 10, 11]),
#     Student("Masha", [7, 9, 9]),
#     Student("Sophie", [12, 11`, 10]),
#     Student("Nika", [10, 11, 8]),
#
# ]
# best = 0
# best_average = []
# for student in students:
#     average = student.average_grade()
#     if average > best:
#         best = average
#         best_average = [student]
#     elif average == best:
#         best_average.append(student)
# for student in best_average:
#     print(f'Найкращий результат - {student}')

#4

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        if amount <= 0:
            print("Не можна начислювати від'ємну суму")
            return self
        self.balance += amount
        return self
    def withdraw(self, amount):
        if amount <= 0:
            print("Не можна знімати від'ємну суму")
            return self
        if self.balance < amount:
            print(f"Недостатньо коштів для -{amount}")
            return self
        self.balance -= amount
        return self
    def info(self):
        print(f'{self.owner}: баланс {self.balance}')

wallet1 = BankAccount("Ivan", 1000)
wallet2 = BankAccount("Olha", 700)
wallet1.deposit(-500)
wallet1.withdraw(300)
wallet1.withdraw(2000)
wallet2.withdraw(-200)
wallet2.deposit(100)
wallet1.info()
wallet2.info()