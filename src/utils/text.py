"""
Utilities for text output
"""

import time

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