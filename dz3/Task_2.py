numbers = input("Введите число, состоящее из четырех чисел: ")
proisvedenie = 1
for symbol in numbers:
    proisvedenie *= int(symbol)
print(proisvedenie)