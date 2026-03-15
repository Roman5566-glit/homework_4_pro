class UnknownOperationError(Exception):
    """Исключение для неизвестной операции"""
    pass


def calculator():
    """Простой консольный калькулятор"""
    try:
        a = float(input("Введите первое число: "))
        op = input("Введите операцию (+ - * /): ")
        b = float(input("Введите второе число: "))

        if op == "+":
            print("Результат:", a + b)

        elif op == "-":
            print("Результат:", a - b)

        elif op == "*":
            print("Результат:", a * b)

        elif op == "/":
            print("Результат:", a / b)

        else:
            raise UnknownOperationError("Неизвестная операция")

    except ZeroDivisionError:
        print("Ошибка: деление на ноль")

    except ValueError:
        print("Ошибка: введено не число")

    except UnknownOperationError as exc:
        print("Ошибка:", exc)

    except OverflowError:
        print("Ошибка: переполнение числа")

    finally:
        print("Работа калькулятора завершена")


calculator()
