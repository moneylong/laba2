import random

# Генерируем список случайных чисел от 0 до 200
random_numbers = [random.randint(0, 200) for _ in range(10)]

# Запрашиваем у пользователя число X
X = int(input("Введите число X: "))

# Создаем лямбда-функцию для проверки на кратность
is_multiple_of_X = lambda num: num % X == 0

# Фильтруем список случайных чисел
multiples = list(filter(is_multiple_of_X, random_numbers))

# Выводим найденные числа
print(f"Числа, кратные {X}:")
for num in multiples:
    print(num)