from cards import *



class Game:
    p1: Player
    p2: Player
    
    def __init__(self) -> None:
        self.p1 = Player()
        self.p2 = Player()

    def player_turn(self, player: Player, opponent: Player):
        used_fractions = {"Империя": 0, # Империя
                            "Гильдия": 0, # Гильдия
                            "Культ смерти": 0, # Культ смерти
                            "Дикари": 0} # Дикари
        player.play_hand()
        for i, card in enumerate(player.active_cards, 1):
            if card.fraction:
                used_fractions[card.fraction] += 1
            print(i, card)
        
        while player.have_playable_cards():
            choice = int(input("Какую карту разыграть: "))
            chosen_card = player.active_cards[choice-1]
            chosen_card.print_properties()
            choice = int(input("Выберите свойство: "))
            if choice == 1:
                chosen_card.primary_property(player, opponent)
            elif choice == 2:
                chosen_card.rotation_property(player, opponent)
            elif choice == 3:
                chosen_card.fraction_property(player, opponent)
            elif choice == 4:
                chosen_card.sacrificial_property(player, opponent)
            if not chosen_card.is_playable() and chosen_card.defense == None:
                player.active_cards.remove(chosen_card)
            player.print_status()

        

if __name__ == "__main__":
    game = Game()
    game.p1.hand.append(Ruby())
    game.p1.hand.append(TorgenStonemason())
    game.p2.hand.append(Ruby())
    game.p2.hand.append(Ruby())
    game.p2.hand.append(Ruby())
    game.player_turn(game.p1, game.p2)









class ElfsCurse:
    def __init__(self):
        self.fraction = "Dikari"
        self.name = "Elf's curse"
        self.cost = 3
        self.has_primary_propery = 1
        self.has_fraction_property = 1
    
    def use_primary_property(self, p1, p2):
        p1.attack += 6
        if len(p2.hand) > 0:
            choice = int(input("Игрок 2: какую карту хотите сбросить? "))
            p2.hand.pop(choice-1)

        p1.active_cards.append(p1.deck[0])
        self.has_primary_propery = 0

    def use_fraction_property(self, p1, p2):
        p1.attack += 3
        self.has_fraction_property = 0

    def recover_props(self):
        self.has_primary_propery = 1
        self.has_fraction_property = 1
    



    
        