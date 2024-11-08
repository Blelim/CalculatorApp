# Визначення функцій
def add(a, b):
    """Повертає суму a і b."""
    return a + b


def subtract(a, b):
    """Повертає різницю між a і b."""
    return a - b


# Головна частина програми
if __name__ == "__main__":
    print("Простий калькулятор")

    # Запитуємо у користувача два числа
    a = float(input("Введіть перше число: "))
    b = float(input("Введіть друге число: "))

    # Запитуємо операцію
    operation = input("Введіть операцію (+ для додавання, - для віднімання): ")

    # Виконуємо обрану операцію та друкуємо результат
    if operation == "+":
        print(f"Результат додавання {a} + {b} = {add(a, b)}")
    elif operation == "-":
        print(f"Результат віднімання {a} - {b} = {subtract(a, b)}")
    else:
        print("Невідома операція. Використовуйте + або -.")