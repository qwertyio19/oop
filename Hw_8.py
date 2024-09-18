"""Try - Except"""

# while True:
#     try:
#         num_1 = float(input("Введите первое число: "))
#         num_2 = float(input("Введите второе число: "))
        
#         addition = num_1 + num_2
#         subtraction = num_1 - num_2
#         multiplication = num_1 * num_2
#         division = num_1 / num_2
        
#         print(f"Сумма: {addition}")
#         print(f"Разность: {subtraction}")
#         print(f"Произведение: {multiplication}")
#         print(f"Деление {division}")
        
#         if addition % 2 == 0:
#             print("Ссумма четная") 
#         else:
#             print("Сумма нечетная")
#             break
        
#     except ValueError:
#         print("Ошибка: Введите числа, а не текст. Попробуйте снова.")
#     except ZeroDivisionError:
#         print("Ошибка: Деление на ноль невозможно. Попробуйте снова.")
        

""" Работа с файлами """

""" 1 """

# file_path = 'foo.txt'  

# try:
#     with open(file_path, 'r') as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print("Файл не найден.")
# except Exception as e:
#     print(f"Произошла ошибка: {e}")
    
    
# file_path = "foo.txt"

# try:
#     with open(file_path, 'r') as file:
#         content = file.read()
#         print(content)
        
# except FileNotFoundError:
#     print("Файл не найден")
# except Exception as e:
#     print(f"Произошла ошибка: {e}")
        

""" 2 """

# file_path = "foo.txt"  
# word = "saidahmad"  

# try:
#     with open(file_path, 'r') as file:
#         content = file.read()
#         if word in content:
#             print(f"Слово '{word}' найдено в файле.")
#         else:
#             print(f"Слово '{word}' не найдено в файле.")
# except FileNotFoundError:
#     print("Файл не найден. Проверьте путь к файлу.")
# except Exception as e:
#     print(f"Произошла ошибка: {e}")
    
    
# file_path = "foo.txt"
# word = "Syimyk"

# try:
#     with open(file_path, 'r') as file:
#         content = file.read()
#         if word in content:
#             print(f"Найдено слово: {word} которую вы искали.")
#         else:
#             print(f"Не найдено слово: {word} которую вы искали.")
# except FileNotFoundError:
#     print("Файл не наден")
# except Exception as e:
#     print("Произошла ошибка")
    
    


""" 3 """

# user_text = input("Введите текст: ")

# file_path = "foo.txt"  

# try:
#     with open(file_path, 'w') as file:
#         file.write(user_text)
#     print(f"Текст успешно сохранён в файл '{file_path}'.")
# except Exception as e:
#     print(f"Произошла ошибка при сохранении файла: {e}")


""" 4 """

# with open('foo.txt', 'r') as source_file, open('destination.txt', 'w') as destination_file:
    
#     content = source_file.read()
#     destination_file.write(content)
    
# print("Копирование завершено.")