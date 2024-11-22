# Подсчитать количество целых чисел в диапазоне от
# 100 до 9999 у которых все цифры разные.

count = 0

for number in range(100, 10000):
    digits = str(number)

    if (digits[0] != digits[1]) != digits[2]):
        # здесь дописать код самому
        count += 1
        print(digits)

print(count)