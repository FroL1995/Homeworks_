# Пользователь вводит с клавиатуры три числа. Необходимо найти сумму чисел, произведение чисел. Результат
# Результат вычислений вывести на экран

# Вариант_1

# num_1 = int(input('Введите первое число: '))
# num_2 = int(input('Введите второе число: '))
# num_3 = int(input('Введите третье число: '))

# summa = num_1 + num_2 + num_3

# print(summa)

# Вариант_2

my_list = [int(i) for i in input("Введите число").split(",")]
summa = 0
proisvedenie = 1
for i in my_list:
    summa += i
    proisvedenie *= i
print(summa, proisvedenie)