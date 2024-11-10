num1=int(input('Введите первое число: '))
num2=int(input('Введите второе число: '))


# Вариант_1

# for i in range(num1, num2 + 1):
#     if i % 7 == 0:
#         print(i)

# Вариант_2

# print(*[i for i in range(num1, num2 + 1) if i % 7 == 0])

# Вариант_3

# [print(i) for i in range(num1,num2+1) if i % 7 == 0] - почему тут так отработает, если print в начале, а условие после консьрукции цикла
