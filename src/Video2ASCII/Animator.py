import os
import time


class Animator:
    """!
    This class is responsible for the animation inside the console.
    """

    def __init__(self, directory):
        self.directory = directory

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def print_ascii_frame(self, file):
        """
        Prints the ASCII text from the specified file.
        :param file:
        :return:
        """
        with open(f"{self.directory}/{file}", 'r') as f:
            ascii_txt = f.read()
            Animator.clear_terminal()
            print(ascii_txt)

    def run_ascii_animation(self):
        """
        Starts the animation of the ASCII art.
        :return:
        """
        for filename in sorted(os.listdir(self.directory)):
            self.print_ascii_frame(filename)
            time.sleep(0.0167)

    @staticmethod
    def clear_terminal():
        os.system('clear' if os.name == 'posix' else 'cls')
