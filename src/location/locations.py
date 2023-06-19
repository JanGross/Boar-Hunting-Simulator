"""Generic Location"""
from utils.input import Option
from utils.text import HeaderStyle
import utils.text as Text
import time

class Location:
    def __init__(self, game, name: str, description: str) -> None:
        super().__init__()
        self.name = name
        self.description = description
        self.options = [Option("Look around", self.look_around)]
        self.game = game

    def look_around(self) -> None:
        Text.print_header(self.name, HeaderStyle.ROUND)
        Text.type(f"{self.description}\n", 0.01, 0.1)
        time.sleep(0.5)

    def enter(self) -> None:
        Text.print_header(self.name, HeaderStyle.ROUND)
        print(f"You enter {self.name}.\n")
        self.game.current_location = self
        time.sleep(0.5)

    def connect_location(self, location) -> None:
        self.options.append(Option(f"Enter {location.name}", location.enter))

class SafeZone(Location):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.options.extend([
            Option("Check stats", self.check_stats),
            Option("Retire", self.game.retire)
        ])

    def check_stats(self) -> None:
        player = self.game.player
        player.check_stats()
        

        

class Shop(Location):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
    
    def look_around(self) -> None:
        print(f"You find yourself in a small shop called {self.name}.\n{self.description}")
    
