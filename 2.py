# Реализовав класс Dog
# Свойства:
# __happiness (целое число) – уровень счастья собаки, значение по умолчанию — 0.
# __name (строка) — имя собаки.
# Методы:
# __init__() — инициализация объекта с начальными параметрами (имя собаки и уровень счастья)
# caress() — повышает уровень счастья собаки на 10 единиц. Также выводит на экран строку «Гав-гав!».
# set_name() — задает новое имя для собаки. Если имя собаки корректно (содержит только буквы), то выводит на экран строку «Теперь собаку зовут <имя>!». В противном случае выводит на экран строку «В имени собаки должны быть только буквы!».
# get_name() — выводит на экран строку «Собаку зовут <имя>»
# bring_item() — принимает на вход название предмета (строка) и расстояние до него (целое число).
# Сценарии работы метода:
# – Если расстояние до предмета <= 100 и уровень счастья собаки >= 10, то выводит на экран строку «<имя> принес(ла) предмет: <предмет>».
# – Если расстояние до предмета > 100, то выводит на экран строку «<предмет> находится слишком далеко!».
# – Если уровень счастья собаки < 10, то выводит на экран строку «<имя> нуждается в вашей заботе!».
class Dog:
    # инициализатор класса
    def __init__(self,happiness,name):
        self.__happiness = happiness
        self.__name = name

    def set_name(self,new_name):
        if new_name.isalpha():
            self.__name = new_name
            print(f"Тепереь собаку зовут{self.__name}")

    def get_name(self):
        return (f" собаку зовут {self.__name}")

    def get_happiness(self):
        return self.__happiness

    def set_happiness(self,new_happiness):
        self.__happiness = new_happiness

    def bring_item(self,element="палка",distans=0):
       if distans <= 100 and self.__happiness >= 10:
           print(f"{self.__name} принёс пердмет : {element} ")
       if distans > 100:
           print(f"{element} находится слишком далеко!")
       if self.__happiness < 10:
            print(f"{self.__name} нуждается в вашей заботе!")

    def caress(self):
        self.__happiness+=10
        print("Гав,гав")

myDog=Dog(happiness=10,name="Граф")
print(myDog.get_name())
myDog.set_name ("Барбос")
myDog.caress()
print(myDog.set_happiness(30))