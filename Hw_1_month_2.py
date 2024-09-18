""" 1 """

class fruits:
    def __init__(self,name, color, weight):
        
        self.name = name
        self.color = color
        self.weight = weight
        
    def info(self):
        print(f"Название фрукта - {self.name}, Цвет фрукта - {self.color}, Вес фрукта - {self.weight}")
        
            
Fruit = fruits("Apple", "Red", "10kg")
Fruit_2 = fruits("Banana", "Yellow", "5kg")
Fruit_3 = fruits("Strawberry", "Red", "20kg")
Fruit.info()
Fruit_2.info()
Fruit_3.info()


""" 2 """

class Book:
    def __init__(self, title, author, pages):
        
        self.title = title
        self.author = author
        self.pages = pages
        
    def info(self):
        print(f"Название книги - {self.title}, Автор книги - {self.author}, Страниц - {self.pages}")
        
    def check_pages(self):
        if self.pages < 100:
            print("Книга тонкая")
        elif self.pages > 100 < 300:
            print("Книга средняя")
        elif self.pages > 300:
            print("Книга толстая")
        
Book = Book("Первый учитель", "Чынгыз Айтматов", 256)
Book.info()
Book.check_pages()         