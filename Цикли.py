while True:
    try:
        x = float(input("Введіть число: "))
        y = float(input("Введіть дільник: "))
        res = x / y
    except ValueError:
        print("Помилка: потрібно вводити тільки числа!")
    except ZeroDivisionError:
        print("Помилка: ділення на нуль неможливе!")
    else:
        print("Результат:", res)
        break
