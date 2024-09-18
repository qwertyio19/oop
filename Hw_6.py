""" 1 """

# def is_even():
#     num_1 = int(input("Введите первое число: "))
#     if num_1 % 2 == 0:
#         print("True")
#     else:
#         print("False")
        
# is_even()

 
""" 2 """

# def factorial(n):
#     n = int(input("Введите число: "))
#     fac = 1
#     for i in range(2, n + 1):
#         fac *= i
#     return fac
    
# print(factorial(5))


""" 3 """        

# def spisok(n):
#     return[num for num in n if num % 2 == 0]
# n = [1,2,3,4,5,6]
# even_numbers = spisok(n)
# print(even_numbers)

   
""" 4 """

# def str(s):
#     return s[::-1]
# num_1 = "Hello world"
# num_2 = str(num_1)
# print(num_2)


""" 5 """

# def is_palindrome(word):
#     return word == word[::-1]

# def filter_palindromes(words):
#     return [word for word in words if is_palindrome(word)]

# words = ["azat", "madam", "sema", "anna", "kazak", "aktan", "zakaz"]
# palindromes = filter_palindromes(words)
# print(palindromes)  