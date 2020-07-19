from sys import argv
from platform import system as sys
from subprocess import call
from .create import website

class Hell:
    def __init__(self):
        """
        Initialize the project with a constructor.
        """

        self.run()

    def run(self):
        """
        Collect the command line arguments.
        """

        if sys() == "Linux":
            sis = "/"
        elif sys() == "Windows":
            sis = r"\\"

        if len(argv) == 2:
            if argv[1] == "--createwebsite":
                website()
            elif argv[1] == "--runwebsite":
                call(f'python app{sis}run.py', shell=True)
        else:
            print('\033[0;35mYou type it something wrong\n\nTry:\n --createwebsite \n --runwebsite\033[m')
