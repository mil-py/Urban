def personal_sum(numbers):
    res = 0
    incorrect_data = 0

    for n in numbers:
        try:
            res += n

        except TypeError:
            incorrect_data += 1
            print(f"Некорректный тип данных для подсчёта суммы - {n}")

    return (res, incorrect_data)


def calculate_average(numbers):
    aver = 0

    try:
        ps = personal_sum(numbers)
        aver = ps[0] / (len(numbers) - ps[1])
    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
    else:
        return aver


print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
