import random

def get_user_choice():
    user_choice = input("Выберите камень (k), ножницы (n) или бумагу (b): ")
    return user_choice

def get_computer_choice():
    choices = ['k', 'n', 'b']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Ничья!"
    elif (user_choice == 'k' and computer_choice == 'n') or (user_choice == 'n' and computer_choice == 'b') or (user_choice == 'b' and computer_choice == 'k'):
        return "Вы победили!"
    else:
        return "Компьютер победил!"

def main():
    print("Добро пожаловать в игру 'Камень-Ножницы-Бумага'!")
    
    while True:
        user_choice = get_user_choice()
        if user_choice not in ['k', 'n', 'b']:
            print("Некорректный выбор. Попробуйте снова.")
            continue
        
        computer_choice = get_computer_choice()
        print(f"Компьютер выбрал {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        play_again = input("Хотите сыграть еще раз? (да/нет): ")
        if play_again.lower() != 'да':
            break

if __name__ == "__main__":
    main()
