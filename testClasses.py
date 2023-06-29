
class House():
    """Описание дома"""
    def __init__(self, street, number):
        """Свойства дома"""
        self.street = street
        self.number = number
        self.age = 25 # аргумент по умолчанию

    def build(self):
        """Строит дом"""
        print(f"Дом на улице {self.street} под номером {self.number} построен!")

House1 = House("Kovalevskaya", 45) #создаем объекты на основе класса
House2 = House("Moskovskaya", 15)

class prospektHouse(House): # наследуем атрибуты из класса House
    """дома на проспекте"""
    def __init__(self, prospekt, number): #
        super().__init__(self, number)
        self.prospekt = prospekt

PrHouse = prospektHouse("Leninskiy", 74)
print(PrHouse.prospekt)