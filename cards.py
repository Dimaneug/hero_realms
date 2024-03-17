from player import Player

# Базовый класс для всех карт

# # Раннее объявление, чтобы избежать ошибки
# class Player:
#     pass

class Card:
    fraction: str # Фракция
    name: str # Название карты
    cost: int # Цена
    defense: int # Кол-во очков защиты
    guard: bool # Является ли карта стражем
    # Ниже описаны разные свойства карт
    # -1 нет такого свойства
    # 0 свойство было использовано
    # 1 свойство можно использовать
    has_primary_property: int # Первичное свойство
    has_rotation_property: int # Свойство поворота
    has_fraction_property: int # Союзное свойство
    has_sacrificial_property: int # Жертвенное свойство
    
    # Инициализация карты
    def __init__(self) -> None:
        self.fraction = None
        self.name = None
        self.cost = None
        self.defense = None
        self.guard = None
        self.has_primary_property = -1
        self.has_rotation_property = -1
        self.has_fraction_property = -1
        self.has_sacrificial_property = -1
    
    def primary_property(self, p1: Player, p2: Player):
        pass

    def fraction_property(self, p1: Player, p2: Player):
        pass

    def rotation_property(self, p1: Player, p2: Player):
        pass

    def sacrificial_property(self, p1: Player, p2: Player):
        pass

    def recover_props(self):
        pass

    def is_playable(self) -> bool:
        return (self.has_primary_property > 0 
                or self.has_rotation_property > 0 
                or self.has_fraction_property > 0 
                or self.has_sacrificial_property > 0)
    
    def print_properties(self):
        if not self.is_playable:
            return
        if (self.has_primary_property > 0):
            print("1 Первичное свойство")
        if (self.has_rotation_property > 0):
            print("2 Cвойство поворота")
        if (self.has_fraction_property > 0):
            print("3 Союзное свойство")
        if (self.has_sacrificial_property > 0):
            print("4 Жертвенное свойство")

    def __str__(self) -> str:
        return f"{self.name}: Фракция: {self.fraction}, Стоимость: {self.cost}"
    


class Ruby(Card):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Рубин"
        self.has_primary_property = 1

    def primary_property(self, p1: Player, p2: Player):
        p1.gold += 2
        self.has_primary_property = 0
        print("Вам добавлено 2 золота!")


class TorgenStonemason(Card):
    def __init__(self) -> None:
        super().__init__()
        self.fraction = "Дикари"
        self.name = "Торген Камнелом"
        self.cost = 7
        self.defense = 7
        self.guard = True
        self.has_rotation_property = 1

    def rotation_property(self, p1: Player, p2: Player):
        p1.attack += 4
        p2.print_hand()
        choice = int(input("Какую карту хочет сбросить противник: "))
        p2.hand.pop(choice-1)
        self.has_rotation_property = 0

    def recover_props(self):
        self.has_rotation_property = 1



class Manny(Card):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Манета"
        self.has_primary_property = 1

    def primary_property(self, p1: Player, p2: Player):
        p1.gold += 1
        self.has_primary_property = 0
        print("Вам добавлено 1 золота!")