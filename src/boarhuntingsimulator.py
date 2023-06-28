#!/usr/bin/env python3

"""  Boar Hunting Simulator 2022"""

from operator import truediv
from data import MenuText as mt
import utils.text as Text
from utils.text import HeaderStyle
from location.locations import *
from player import Player
from utils.input import Menu, Option


class Game:
    def __init__(self) -> None:
        self.player = Player()
        #ToDo: move this out of the main file
        locations = { 
            "City": SafeZone(self, "Mayberry", "You find yourself in the small rural town of Mayberry. \nThe town is quaint and charming, with a population of only a few hundred people. \nIt is surrounded by a thick forest, and the only way to get here is on foot. \nThere are a few shops and businesses around."),
            "Berrys": SafeZone(self, "Berry's Brews", "The tavern is abuzz with lively chatter and laughter, creating a warm and inviting atmosphere. The patrons, a diverse mix of locals and travelers, gather around wooden tables and cozy booths, each immersed in their own tales and mugs of frothy drinks."),
            "Forest": Location(self, "the Forest", "You find yourself in a warm and lush oak forest. \nThe dense trees provide plenty of cover from the sun, and the forest floor is carpeted with a thick layer of leaves. \nYou hear the sound of birdsong all around you, and the occasional rustle of small animals in the undergrowth."),
        }

        locations["City"].connect_location(locations["Forest"])
        locations["City"].connect_location(locations["Berrys"], hidden=True)
        locations["Berrys"].connect_location(locations["City"])
        locations["Forest"].connect_location(locations["City"])

        self.current_location = locations["City"]
        self.quit = False
        self.main()

    def retire(self):
        Text.type(mt.retire_text)
        self.quit = True

    def main(self):
        Text.clear()
        Text.print_header("Welcome", HeaderStyle.ROUND)
        Text.type(mt.intro_text, delay=0.01, newline_delay=1.0)
        while not self.quit:
            Menu("What would you like to do?", self.current_location.get_options()).show()



if __name__ == "__main__":
    game = Game()
    print("Process exited")
    exit(0)