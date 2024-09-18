# """ Наследование и множественное наследование """

# class Game:
#     def __init__(self,game_name, graphics, game_year, company ):
#         self.game_name = game_name
#         self.graphics = graphics
#         self.game_year = game_year
#         self.company = company
        
#     def info(self):
#         print(f"Название игры - {self.game_name}, максимальная графика - {self.graphics}, дата релиза - {self.game_year}, создатели - {self.company}")
        
# game = Game("CsGO", "FULL HD 4K", 2013, "Valve")
# game.info()






# class Roblox(Game):
#     def __init__(self, game_name, graphics, game_year, company, multiplayer):
#         super().__init__(game_name, graphics, game_year, company)
#         # Game.__init__(game_name, graphics, game_year, company)
#         self.multiplayer = multiplayer
#         self.name = "player"
#         self.gender = "man"
#         self.skin = "VIP"
#         self.hp = 100
        
#     def info_player(self):
#         print(f"Игрок - {self.name}, Пол - {self.gender}, Облик - {self.skin}, Здоровье - {self.hp}")
#         print("===============\nROBLOX - запустился и готов к игре")
        
#     def edit_player(self):
#         name = input("ВВедите имя игрока: ")
#         gender = input("Введите пол игрока: ")
#         skin = input("Введите облик персонажа: ")
#         self.name = name
#         selfgender = gender
#         self.skin = skin
        
# roblox = Roblox("Roblox", "ULTRA", "2006", "Roblox Corporation", "Yes")
# # roblox.info()
# # roblox.edit_player()
# # roblox.info_player()




# class Snake(Roblox):
#     def __init__(self, name, gender, skin):
#         self.name = name
#         self.gender = gender
#         self.skin = skin
#         self.hp = 100
        
# snake = Snake("Бека", "Муж", "Platinium")
# snake.info_player()











class Animal:
    def __init__(self, name, eat, sleep):
        self.name = name
        self.eat = eat
        self.sleep = sleep
        
    def info(self):
        print(f"Имя животного - {self.name}, Животное ест - {self.eat}, Животное спит в - {self.sleep}")

        
animal = Animal("Лев", "мясо", "19:00")



class Walker(Animal):
    def __init__(self, name, eat, sleep, walk):
        super().__init__(name, eat, sleep)
        self.walk = walk
        
    def info_walk(self):
        print(f"Лев - {self.walk}")

walk = Walker("Лев", "мясо", "19:00", "Ходит")
walk.info()
walk.info_walk()        
        


class Swimmer(Animal):
    def __init__(self, name, eat, sleep, swim):
        super().__init__(name, eat, sleep)
        self.swim = swim
        
    def info_swim(self):
        print(f"Дельфин - {self.swim}")        
        
swim = Swimmer("Дельфин", "Рыб", "20:00", "Плавает")
swim.info()
swim.info_swim()


class Flyer(Animal):
    def __init__(self, name, eat, sleep, fly):
        super().__init__(name, eat, sleep)
        self.fly = fly
        
    def info_fly(self):
        print(f"Чайка - {self.fly}")
        
fly = Flyer("Чайка", "Рыб и насекомых", "23:00", "Летает")
fly.info()
fly.info_fly()



class Penguin(Animal):
    def __init__(self, name, eat, sleep, walk, swim):
        super().__init__(name, eat, sleep)
        self.walk = walk
        self.swim = swim
        
    def describe(self):
        print(f"Пингвин - {self.walk}, {self.swim}")
        
penguin = Penguin("Пингвин", "Рыб", "20:00", "ходит", "и плавает")
penguin.info()
penguin.describe()



class Duck(Animal):
    def __init__(self, name, eat, sleep, walk, swim, fly):
        super().__init__(name, eat, sleep)
        self.walk = walk
        self.swim = swim
        self.fly = fly
        
    def describe(self):
        print(f"Утка - {self.walk}, {self.swim}, {self.fly}")
        
duck = Duck("Утка", "насекомых", "20:00", "ходит", "плавает", "и летает")
duck.info()
duck.describe()



class Bat(Animal):
    def __init__(self, name, eat, sleep, fly):
        super().__init__(name, eat, sleep)
        self.fly = fly
        
    def describe(self):
        print(f"Летучая мышь - {self.fly}")
        
bat = Bat("Летучая мышь", "насекомых", "днём", "может летать")
bat.info()
bat.describe()