"""
Utilities for text output
"""

import time, os
from enum import IntEnum
from typing import List, Dict

class HeaderStyle(IntEnum):
    LIGHT = 0,
    BOLD = 1
    ROUND = 2

def type(text: str, delay: float = 0.05, newline_delay: float = 0.0) -> None:
    """ Prints the given text, one character at a time, with a delay between each character.

        Arguments:  
            text: The text to be printed.  
            delay: The delay between each character. (Default 0.05)
            newline_delay: The delay between each newline. (Default 0.0)
    """
    for char in text:
        print(char, end="", flush=True)
        if (char == "\n"):
            time.sleep(newline_delay)
        time.sleep(delay)

def clear() -> None:
    os.system('cls' if os.name=='nt' else 'clear')

def print_header(title: str, style: HeaderStyle = HeaderStyle.LIGHT, padding: int = 1, length: int = 0):
    """ Prints the Title wrapped by a decoration char

        Arguments:
            title: Title to be printed
            style: Changes the viasual style of the header.
                   Light has single line wraps, bold double lines wraps
                   Round has single lines with round corners
            length: Total length the header has to fill
    """

    #If no length is defined, use the terminal width (-2 to avoid any line breaks)
    length = length if length > 0 else os.get_terminal_size()[0] - 2 
    
    title = f"{' ' * padding}{title}{' ' * padding}"

    characters: List[Dict[str, str]] = [
        { 'line': '─', 'tj_left': '┤', 'corner_tl': '┌', 'corner_tr': '┐', 'corner_bl': '└', 'corner_br': '┘', 'tj_right': '├'},
        { 'line': '═', 'tj_left': '╣', 'corner_tl': '╔', 'corner_tr': '╗', 'corner_bl': '╚', 'corner_br': '╝', 'tj_right': '╠'},
        { 'line': '─', 'tj_left': '┤', 'corner_tl': '╭', 'corner_tr': '╮', 'corner_bl': '╰', 'corner_br': '╯', 'tj_right': '├'},
    ]

    title_length: int = len(title)
    pre_wrap_length: int = int(length / 2) - int(title_length / 2)
    post_wrap_length: int = length - pre_wrap_length - title_length

    print(' ' * pre_wrap_length + characters[style]['corner_tl'] + characters[style]['line'] * title_length + characters[style]['corner_tr'])
    print(f"{characters[style]['line'] * pre_wrap_length}{characters[style]['tj_left']}{title}{characters[style]['tj_right']}{characters[style]['line'] * post_wrap_length}")
    print(' ' * pre_wrap_length + characters[style]['corner_bl'] + characters[style]['line'] * title_length + characters[style]['corner_br'])

