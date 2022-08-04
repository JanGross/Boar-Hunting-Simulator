#!/usr/bin/env python3

"""  Boar Hunting Simulator 2022"""

import utils.text as Text
from data import MenuText as mt

def main():
    Text.type(mt.intro_text, delay=0.01, newline_delay=1.0)

if __name__ == "__main__":
    main()
    input()
    exit(0)