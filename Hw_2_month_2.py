""" Домашнее задание """


class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married
        
    def introduce_myself(self):
        print(f"Полное имя - {self.fullname}, Возраст - {self.age}, Женат - {self.is_married}")
        
        
class Teacher(Person):
    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)
        self.experience = experience
        self.salary = 25000
        
    
        if experience < 3:
            print(f"К стандартной зарплате прибавляется бонус 3000 за каждые три года опыта.\nОбщая зарплата - {self.salary} + 0\nВаш бонус 0")
        elif experience == 3 :
            print(f"К стандартной зарплате прибавляется бонус 3000 за каждые три года опыта.\nОбщая зарплата - {self.salary + 3000}\nВаш бонус 3000")
        elif experience < 6:
            print(f"К стандартной зарплате прибавляется бонус 3000 за каждые три года опыта.\nОбщая зарплата - {self.salary + 3000}\nВаш бонус 3000")
        elif experience == 6:
            print(f"К стандартной зарплате прибавляется бонус 3000 за каждые три года опыта.\nОбщая зарплата - {self.salary + 6000}\nВаш бонус 6000")
        elif experience < 9:
            print(f"К стандартной зарплате прибавляется бонус 3000 за каждые три года опыта.\nОбщая зарплата - {self.salary + 6000}\nВаш бонус 6000")
        elif experience == 9:
            print(f"К стандартной зарплате прибавляется бонус 3000 за каждые три года опыта.\nОбщая зарплата - {self.salary + 9000}\nВаш бонус 9000")
        elif experience < 12:
            print(f"К стандартной зарплате прибавляется бонус 3000 за каждые три года опыта.\nОбщая зарплата - {self.salary + 9000}\nВаш бонус 9000")
        elif experience == 12:
            print(f"К стандартной зарплате прибавляется бонус 3000 за каждые три года опыта.\nОбщая зарплата - {self.salary + 12000}\nВаш бонус 12000")
        elif experience > 12:
            print(f"К стандартной зарплате прибавляется бонус 3000 за каждые три года опыта.\nОбщая зарплата - {self.salary + 12000}\nВаш бонус 12000")
                
            
teacher = Teacher("Сергей Петров", 40, "Да", 10)
teacher.introduce_myself()