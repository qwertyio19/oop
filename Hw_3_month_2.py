""" Домашнее задание """


class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory
        
    def make_computation(self):
        addition = self.__cpu + self.__memory
        print(f"Результат сложения: {self.__cpu} + {self.__memory} = {addition}")
        
        subtraction = self.__cpu - self.__memory
        print(f"Результат вычитания: {self.__cpu} - {self.__memory} = {subtraction}")
        
        multiplication = self.__cpu * self.__memory
        print(f"Результат умножения: {self.__cpu} * {self.__memory} = {multiplication}")
        
        division = self.__cpu / self.__memory
        print(f"Результат деления: {self.__cpu} / {self.__memory} = {division}")
        
    
    def get(self):
        return self.__cpu, self.__memory 
    
    def info(self):
        print(f"Информация о компютере - CPU: {self.__cpu}, MEMORY: {self.__memory}")
        



class Laptop(Computer):
    def __init__(self, cpu, memory, memory_card):
        super().__init__(cpu, memory)
        self.__memory_card = memory_card
        
    def get(self):
        return self.__memory_card
    
    def info(self):
        print(f"Информация о компютере - CPU: {self.__cpu}, MEMORY: {self.__memory}")
        
computer = Computer(8, 16)
computer.make_computation()
print(computer.info())