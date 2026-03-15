def average_from_file(filename):
    """Читает числа из файла и считает среднее"""

    try:
        with open(filename, "r") as file:
            lines = file.readlines()

        if len(lines) == 0:
            print("Файл пуст")
            return

        numbers = [float(i.strip()) for i in lines]

        if len(numbers) == 1:
            print("В файле только одно число:", numbers[0])
            return

        avg = sum(numbers) / len(numbers)
        print("Среднее арифметическое:", avg)

    except FileNotFoundError:
        print("Ошибка: файл не найден")

    except ValueError:
        print("Ошибка: файл содержит нечисловые данные")


average_from_file("numbers.txt")
