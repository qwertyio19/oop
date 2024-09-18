""" Арифметические операции. Переменные."""

# if True:
#     print("Hello World")
    
# a = 10
# b = 5
# if a < b:
#     print("Hello")
# else:
#     print("Hello")

# while True:
    
#    a = int(input("Введите первое число: "))
#    b = int(input("Введите второе число: "))
#    if a > b:
#     print(f"Первое число больше {b}")
#    else:
#     print(f"Второе число больше {a}")


# a = int(input("Введите число: "))

# if a % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")


# for a in range(3):
#     print(a)

# for num in range(40, 51):
#     if num == 45:
#        continue
#     print(num)


# for nums in range(1000, 990, -1):
#     print(nums)


# even_nums = [x for x in range(30) if x % 2 == 0]
# print(even_nums)


# count = 1 

# while count <= 10:
#     print(count, end=' ')
#     count += 1


# num = 0
# control = True
# while num < 10:
#     num += 1
    
# num = 0
# control = True
# while control:
#     if num == 10:
#         control = False
#     num += 1


# x = 20
# y = 30
# while x < y:
#     print(x, end= ' ')
#     x = x + 3


# word = "pythonchick"
# while word:
#     print(word, end=" ")
#     word = word[:-1]
    
    
# counter = 1
# while True:
#     if counter == 10:
#         break
#     counter += 1

# z = 10
# while z:
#     z -= 1
#     if z % 2 != 0:
#         continue
#     print(z,"\n")


# import time

# while True:
#     print("Бесконечный цикл")
#     break


# i = 5
# while i != 0:
#     print("Hello world!")
#     i -= 1



# class dumbbel:
#     def __init__(self, name, weight, color):
        
#         self.name = name
#         self.weight = weight
#         self.color = color
        
#     def info(self):
#         print(f"Название - {self.name}, Вес - {self.weight}, Цвет - {self.color}")
        
#     def strength(self):
#         if self.weight < 30:
#             print("Слабак")
#         elif self.weight < 40:
#             print("Нормально")
#         elif self.weight > 40:
#             print("Сильный")

# Dumbbel = dumbbel("Гантель", 50, "Коричневый")
# Dumbbel.info()
# Dumbbel.strength()



# class Person:
#     def init(self, fullname, age, is_married):
#         self.fullname = fullname
#         self.age = age
#         self.is_married = is_married

#     def introduce_myself(self):
#         married_status = "замужем/женат" if self.is_married else "не замужем/не женат"
#         print(f"Меня зовут {self.fullname}. Мне {self.age} лет. Я {married_status}.")

# class Teacher(Person):
#     salary = 0

#     def init(self, fullname, age, is_married, experience):
#         super().init(fullname, age, is_married)
#         self.experience = experience

#     def calculate_salary(self, base_salary):
#         bonus = (self.experience // 3) * 3000
#         self.salary = base_salary + bonus
#         return self.salary

#     def introduce_myself(self):
#         super().introduce_myself()
#         print(f"Опыт работы: {self.experience} лет. Зарплата: {self.salary}.")

# # Создание объекта учителя
# teacher = Teacher("Иван Иванов", 40, True, 10)

# # Представляемся и считаем зарплату
# teacher.introduce_myself()
# salary = teacher.calculate_salary(50000)
# print(f"Расчетная зарплата: {salary} руб.") 

