
class Card:
    pass

class Player:
    active_cards: list[Card]
    hand: list[Card]
    gold: int
    attack: int
    hp: int
    discard_deck: list[Card]

    def __init__(self) -> None:
        self.hand = []
        self.active_cards = []
        self.discard_deck = []
        self.gold = 0
        self.attack = 0
        self.hp = 50

    def play_hand(self):
        for card in self.hand:
            self.active_cards.append(card)
        self.hand.clear()

    def print_status(self) -> None:
        print("-"*20)
        print(f"Золото: {self.gold}\nСила: {self.attack}")
        print("Ваши карты:")
        for i, card in enumerate(self.active_cards, 1):
            print(i, card)
        print("-"*20)

    def print_hand(self) -> None:
        print("-"*20)
        for i, card in enumerate(self.hand, 1):
            print(i, card)
        print("-"*20)

    def have_playable_cards(self) -> bool:
        for card in self.active_cards:
            if card.is_playable():
                return True
        return False