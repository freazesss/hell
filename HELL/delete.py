from os import system
import os.path

class delete:
    def __init__(self):
        self.run()
    def run(self):
        qes = input("\033[0;32mConfirm (Y/N):\033[m").upper()
        if qes == "Y":
            system('rm -R app/')
        if qes == "N":
            return