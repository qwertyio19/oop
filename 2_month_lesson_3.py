""" Инкапсуляция """


class PublicExample:
    def __init__(self, value):
        self.value = value #Публичный атрибут
        
    def info(self):
        print (self.value) #Публичный метод
    
public = PublicExample(42)
public.info() #Вызов публичного метода


class PublicExample:
    def __init__(self, value):
        self.value = value #Публичный атрибут
        
    def info(self):
        return self.value #Публичный метод
    
public = PublicExample(42)
print (public.info()) #Вызов публичного метода
print (public.value) #Публичный атрибут


class ProtectedExample:
    def __init__(self, value):
        self._value = value #Защищенный атрибут
        
    def info(self):
        return self._value #Защищенный атрибут
    
protected = ProtectedExample(50)
print (protected.info()) #Это работает, но это противаречит принципам инкапсуляции
print (protected._value) #Можно получить значение напрямую, но это не рекомендуется


#Приватный

class PrivateExample:
    def __init__(self, value):
        self.__value = value #приватный атрибут
        
    def __info(self):
        return self.__value #Приватный метод
    
    def accesss_private(self):
        return self.__info() #Публичный метод , где мы получаем доступ к приватному атрибуту
    
private = PrivateExample(300)
#Прямой вызов приватного метода вызовит ошибку
# print(private.__info())
#Прямой вызов приватного атрибута вывозит ошибку
# private(private.__value)

#доступ через публичный метод
print(private.accesss_private())

#Доступ к приватному атрибуту через (name mangling)
print(private._PrivateExample__value)





class MobileLegends:
    def __init__(self, person, rang, item, history):
        self.person = person#Публичный
        self.rang = rang#Публичный
        self._item = item#Защищенный
        self.__history = history #Приватный
        
        
    def player_info(self):
        print(f"Персонаж - {self.person}, Ранг - {self.rang}, ")