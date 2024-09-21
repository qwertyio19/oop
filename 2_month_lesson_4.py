""" Полиморфизм """


class PaymentMethod:
    def pay(self, amount):
        pass
    
class CreditCard(PaymentMethod):
    def pay(self, amount):
        return f"Сумма {amount}, оплачивается по кредитной карте"
    
class PayPal(PaymentMethod):
    def pay(self, amount):
        return f"Сумма {amount}, оплачивается по PayPal"
    
class BankTransfer(PaymentMethod):
    def pay(self, amount):
        return f"Сумма {amount}, оплачивается по банковскому переводу"
    
payments = [CreditCard(),  PayPal(), BankTransfer()]

for payment in payments:
    print(payment.pay(1000))



# class Cat:
#     def __init__(self, name, preferences):
#         self.name = name
#         self.preferences = preferences
        
#     def info(self):
#         print(f"Я кот. Меня зовут {self.name}. Мне {self.preferences} года")
        
#     def make_sound(self):
#         print("мяу")
        
        
# class Dog:
#     def __init__(self, name, preferences):
#         self.name = name
#         self.preferences = preferences
        
#     def info(self):
#         print(f"Я собака. Меня зовут {self.name}. Мне {self.preferences} года")
        
#     def make_sound(self):
#         print("гаф")
        
        

# cat = Cat("Tom", 2)
# dog = Dog("Muhtar", 3)

# for animal in(cat, dog):
#     animal.info()
#     animal.make_sound()