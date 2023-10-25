import os
import time

class Animator:
    def __init__(self, directory):
        self.directory = directory

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def print_ascii_frame(self, file):
        with open(f"{self.directory}/{file}", 'r') as f:
            ascii_text = f.read()
            Animator.clear_terminal()
            print(ascii_text)

    def run_ascii_animation(self):
        for filename in sorted(os.listdir(self.directory)):
            self.print_ascii_frame(filename)
            time.sleep(0.1)

    @staticmethod
    def clear_terminal():
        os.system('clear' if os.name == 'posix' else 'cls')