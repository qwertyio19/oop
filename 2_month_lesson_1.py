""" Объектное ориентированные программирования """

# full_name = "Аслан" змеиный регистр
# FullName = "Жибек"  верблюжий регистр

# class Car: #шаблон или же чертеж
#     def __init__(self,marka, model, color): #init это (магический метод) конструктор
#        #Атрибуп объекта
#        self.marka = marka  
#        self.model = model  #self (ссылка на текущий объект)
#        self.color = color
#        #Атрибут класса
#        self.bak = 10
#        self.is_start = False
       
#     def info(self):
#         print(f"Марка машины - {self.marka}, модель - {self.model}, цвет - {self.color}")

#     def start(self):
#         if self.bak > 0:
#            self.is_start = True
#            print(f"Машина {self.marka} - {self.model} заведена")
#         else:
#             print(f"Машина {self.marka} - {self.model} нет топлива")

#     def stop(self):
#         self.is_start = False
#         print(f"Машина {self.marka} - {self.model} заглушено")
        
#     def drive(self, city):
#         if self.is_start == True:
#             print(f"Машина {self.marka} - {self.model} едет в {city}")
#         else:
#             print(f"Машина {self.marka} - {self.model} не заведена")

# bmw = Car("BMW", "M5 F90", "Black")
# bmw.info()
# bmw.start()
# bmw.stop()
# bmw.drive("Дубай") 





# class book:
#     def __init__(self,avtor, book_name, year):
        
#         self.avtor = avtor
#         self.book_name = book_name
#         self.year = year
        
#     def info(self):
#         print(f"Автор - {self.avtor}, Название книги - {self.book_name}, Год - {self.year}")
        
# Book = book("Чынгыз Айтматов", "Первый учитель", "1962")
# Book.info() 







# class fruits:
#     def __init__(self,name, color, weight):
        
#         self.name = name
#         self.color = color
#         self.weight = weight
        
#     def info(self):
#         print(f"Название фрукта - {self.name}, Цвет фрукта - {self.color}, Вес фрукта - {self.weight}")
        
            
# Fruit = fruits("Apple", "Red", "10kg")
# Fruit_2 = fruits("Banana", "Yellow", "5kg")
# Fruit_3 = fruits("Strawberry", "Red", "20kg")
# Fruit.info()
# Fruit_2.info()
# Fruit_3.info()