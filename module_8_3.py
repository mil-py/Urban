class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        try:
            self.__is_valid_vin(vin)

        except IncorrectVinNumber:
            raise
        else:
            self.__vin = vin

        try:
            self.__is_valid_numbers(numbers)

        except IncorrectCarNumbers:
            raise
        else:
            self.__numbers = numbers

    def __is_valid_vin(self, vin):
        if isinstance(vin, int):
            if vin not in range(1000000, 10000000):
                raise IncorrectVinNumber('Неверный диапазон для vin номера')
            return True
        else:
            raise IncorrectVinNumber('Некорректный тип vin номер')

    def __is_valid_numbers(self, nums):
        if isinstance(nums, str):
            if len(nums) != 6:
                raise IncorrectCarNumbers('Неверная длина номера')
            else:
                return True
        else:
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

#---------------------------------------------------------------

try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:

    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
