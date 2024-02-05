# Модификаторы доступа в Python

# создаем класс для моделирования автомобиля
# Создайте класс Car, описывающий автомобиль. Внутри класса должны быть следующие поля:
# color (строка,публичное поле) – цвет машины
# _speed (целое число, защищенное поле) – текущая скорость машины, значение по умолчанию – 0
# __model (строка, приватное поле ) – модель машины
# Также внутри класса Car должен быть метод show_info(), выводящий на экран информацию о машине в следующем формате:
# «Цвет: <цвет>»
# «Текущая скорость: <скорость>»
# «Модель: <модель>»

class Car:
    # инициализатор класс
    def __init__(self, color, speed, model):
        # публичное поле
        self.color = color
        # защищенное поле (одно нижнее подчеркивание)
        self._speed = speed
        # приватное поле (два  нижних подчеркивания)
        self.__model = model

    def show_info(self):
        print(f"Цвет:{self.color}")
        print(f"Текущая скорость:{self._speed}")
        print(f"Модель:{self.__model}")

    def get_model(self):
        return self.__model
    def get_speed(self):
        return self._speed

        # Сеттер — метод, позволяющий безопасным способом обратиться к полю и поменять его значение

    def set_speed(self, new_speed):
        if new_speed > 0:
            self.__speed = new_speed
        else:
            print("Скорость не может быть отрицательной")


#Искажение имени

my_car=Car(color="Blue",speed=100,model="Skyline")
my_car.show_info()
print(my_car.color)
print(my_car._speed)
print(my_car._Car__model)

my_car=Car(color="Синий",speed=100,model="Skyline")
print(my_car.get_model())
my_car.set_speed(-50)

    # Геттеры и сеттеры

    # Геттер — метод, позволяющий безопасным способом обратиться к полю и получить его значение






