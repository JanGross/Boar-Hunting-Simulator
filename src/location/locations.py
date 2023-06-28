"""Generic Location"""
from utils.input import Option
from utils.text import HeaderStyle
from typing import List, Type
import utils.text as Text
import time

class Location:
    def __init__(self, game, name: str, description: str) -> None:
        super().__init__()
        self.name = name
        self.description = description
        self.options: List[Option] = [Option("Look around", self.look_around)]
        self.connections: List[Connection] = []
        self.game = game

    def look_around(self) -> None:
        Text.print_header(self.name, HeaderStyle.ROUND)
        Text.type(f"{self.description}\n", 0.01, 0.1)

        for connection in self.connections:
            if not connection.discovered:
                connection.discover()

        time.sleep(0.5)

    def enter(self) -> None:
        Text.print_header(self.name, HeaderStyle.ROUND)
        print(f"> You enter {self.name}.\n")
        self.game.current_location = self
        time.sleep(0.5)

    def connect_location(self, location, hidden: bool = False) -> None:
        connection: Connection = Connection(location, not hidden)
        self.connections.append(connection)

    def get_options(self) -> List[Option]:
        all_options = []
        for connection in self.connections:
            if connection.discovered:
                all_options.append(Option(f'Enter {connection.target_location.name}', connection.target_location.enter))
        all_options.extend(self.options)
        return all_options


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
    
class Connection:
    def __init__(self, target_location: Location, discovered: bool = True) -> None:
        self.target_location = target_location
        self.discovered = discovered
    
    def discover(self) -> None:
        self.discovered = True
        Text.type(f"> You discovered {self.target_location.name}")