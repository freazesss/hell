from os import system
import os.path
from platform import system as sys

class delete:
    def __init__(self):
        self.run()
    def run(self):
        qes = input("\033[0;32mConfirm (Y/N):\033[m").upper()
        if qes == "Y":
            if sys() == "Linux":
                system('rm -R app/')
            elif sys() == "Windows":
                system('RD /S app/')
        if qes == "N":
            return