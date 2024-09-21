# """ Домашнее задание """


# class Vehicle:
#     def move(self):
#         pass 
    
    
# class Car:
#     def move(self):
#         return f"Машина едет по дороге"
    
    
# class Bicycle:
#     def move(self):
#         return f"Велосипед едет по своему тратуару"
    
    
# class Boat:
#     def move(self):
#         return f"Лодка плывёт по воде"
    
    
# vehicles = [Car(), Bicycle(), Boat()]

# for vehicle in vehicles:
#     print(vehicle.move())
    
    
    
# Базовый класс Vehicle
class Vehicle:
    def move(self):
        print("Транспортное средство движется")
    
    def fuel(self):
        return "Неизвестный тип топлива"

# Подкласс Car
class Car(Vehicle):
    def move(self):
        print("Машина едет по дороге")
    
    def fuel(self):
        return "Бензин или дизель"

# Подкласс Bicycle
class Bicycle(Vehicle):
    def move(self):
        print("Велосипед едет по велосипедной дорожке")
    
    def fuel(self):
        return "Человеческая сила"

# Подкласс Boat
class Boat(Vehicle):
    def move(self):
        print("Лодка плывет по воде")
    
    def fuel(self):
        return "Дизель или электричество"

# Создание списка объектов разных типов транспортных средств
vehicles = [Car(), Bicycle(), Boat()]

# Демонстрация работы метода move() для каждого объекта
for vehicle in vehicles:
    vehicle.move()

# Демонстрация работы метода fuel() для каждого объекта
for vehicle in vehicles:
    print(f"{vehicle.class.name} использует {vehicle.fuel()} для передвижения.")