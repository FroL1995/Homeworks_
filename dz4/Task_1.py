# Пользователь вводит с клавиатуры три числа. В зависимости от выбора пользователя программа выводит
# на экран сумму трёх чисел или произведение трёх чисел.

# Вариант_1

# numbers = [int(i) for i in input("Введите три числа: ") if i.isdigit()]
# sign = input("Введите знак: ")
# multiple = 1
# if sign == "*":
#     for i in numbers:
#         multiple *= i
#     print(multiple)
# elif sign == "+":
#     summa = sum(numbers)
#     print(summa)
# else:
#     print("Я не знаю такого знака!")

# Вариант_2

# numbers = [int(i) for i in input('Введите три числа: ') if i.isdigit()]
# sign = input("Введите знак")
# if sign == '*':
#     multiple = 1
#     for i in numbers:
#         multiple *=i
#     print(multiple)
# elif sign == '+':
#     summa = 0
#     for i in numbers:
#         summa +=i
#     print(summa)