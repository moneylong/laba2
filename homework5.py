def get_number():
    """Возвращает список нечетных чисел от 0 до 29"""
    return [i for i in range(30) if i % 2 != 0]

def find_odd_numbers():
    """Находит и выводит первое, пятое и последнее нечетные числа"""
    odd_numbers = get_number()
    
    # Находим первое значение
    first_value = odd_numbers[0]
    
    # Находим пятое значение
    fifth_value = odd_numbers[4]
    
    # Находим последнее значение
    last_value = odd_numbers[-1]
    
    print(f"Первое значение: {first_value}")
    print(f"Пятое значение: {fifth_value}")
    print(f"Последнее значение: {last_value}")

# Вызываем функцию
find_odd_numbers()