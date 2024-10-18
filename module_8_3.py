class IncorrectVinNumber(Exception):
    def __init__(self,message):
        self.message = message

class IncorrectCarNumber(Exception):
    def __init__(self,message):
        self.message = message
class Car:
    def __is_valid_vin(self, vin_numbers):
        if isinstance(vin_numbers, int):
            if 1000000 <= vin_numbers <= 9999999:
                return True
            else:
                raise IncorrectVinNumber('Неверный диапазон для vin номера')
        else:
            raise IncorrectVinNumber('Некорректный тип vin номер')

    def __is_valid_numbers(self, numbers):
        if isinstance(numbers, str):
            if len(numbers) == 6:
                return True
            else:
                raise IncorrectCarNumber('Неверная длина номера')
        else:
            raise IncorrectCarNumber('Некорректный тип данных для номеров')
    def __init__(self, model, vin_numbers, numbers):
        self.model = model
        if self.__is_valid_vin(vin_numbers) == True:
            self.vin = vin_numbers
        if self.__is_valid_numbers(numbers) == True:
            self.__numbers = numbers


try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumber as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumber as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumber as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')
