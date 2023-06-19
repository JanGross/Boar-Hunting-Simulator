"""
Utility to show a seletion menu
"""
import time
import utils.text as Text

class Option(object):
    def __init__(self, text: str, callback: callable) -> None:
        self.text = text
        self.callback = callback

class Menu(object):
    def __init__(self, title: str, options: list) -> None:
        self.title = title
        self.options = options

    def show(self) -> int:
        print(f"\n{self.title}")

        for i, option in enumerate(self.options):
            print(f"{i+1}. {option.text}")
            time.sleep(0.25)
        selected = int(input(f"Select an option [1-{len(self.options)}]: "))

        if selected > len(self.options):
            print("Invalid option.")
            time.sleep(0.5)
            self.show()
        else:
            Text.clear()
            if self.options[selected-1].callback is not None:
                self.options[selected-1].callback()

        return selected