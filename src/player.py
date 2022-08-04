import utils.text as Text

class Player(object):
    def __init__(self) -> None:
        self.name = ""
        self.gold = 10
        self.score = 0
        self.mana = 100
        self.health = 100
        self.current_location = None
        self.consumables = { "health" : 0, "mana" : 0 }
        self.gear = { "sword" : 0, "armor" : 0, "shield" : None, "staff" : None }

    def check_stats(self):
        print("You check your stats.")
        print(f"💖 Health: {self.health}")
        print(f"✨ Mana: {self.mana}")
        print(f"💰 Gold: {self.gold}")

    def damage(self, amount: int) -> None:
        self.health -= amount
        print(f"You take {amount} damage.")
        if self.health < 0:
            self.die()
    
    def heal(self, amount: int) -> None:
        self.health += amount
        if self.health > 100:
            self.health = 100
        print(f"You heal {amount} health.")

    def die(self) -> None:
        Text.type("You die.")
    