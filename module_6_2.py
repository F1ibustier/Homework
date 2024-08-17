# Доступ к свойствам родителя. Переопределение свойств
# coded by f1ibustier

class Vehicle:
    __COLOUR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, __model, __engine_power, __colour):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__colour = __colour

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_colour(self):
        return f'Цвет: {self.__colour}'

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_colour())
        print(f'Владелец: {self.owner}')

    def set_colour(self, new_colour):
        if new_colour.lower() in self.__COLOUR_VARIANTS:
            self.__colour = new_colour
        else:
            print(f'Нельзя сменить цвет на {new_colour}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_colour('Pink')
vehicle1.set_colour('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
