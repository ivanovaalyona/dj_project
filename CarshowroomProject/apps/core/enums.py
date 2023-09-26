from enum import Enum


class CarBrandEnum(Enum):
    TOYOTA = 'toyota'
    MAZDA = 'mazda'
    SUBARU = 'subaru'
    LEXUS = 'lexus'
    HONDA = 'honda'
    VOLKSWAGEN = 'volkswagen'
    VOLVO = 'volvo'
    BMW = 'bmw'
    FORD = 'ford'

    @classmethod
    def choices(cls):
        return [(item.value, item.name) for item in cls]


class CarTypeEnum(Enum):
    CABRIOLET = 'cabriolet'
    LIMOUSINE = 'limousine'
    SPORT_CAR = 'sport car'
    CROSSOVER = 'crossover'
    PICKUP = 'pickup'
    SEDAN = 'sedan'
    COUPE = 'coupe'

    @classmethod
    def choices(cls):
        return [(item.value, item.name) for item in cls]


class CarFuelEnum(Enum):
    PETROL = 'petrol'
    DIESEL = 'diesel'
    ELECTRIC = 'electric'

    @classmethod
    def choices(cls):
        return [(item.value, item.name) for item in cls]

