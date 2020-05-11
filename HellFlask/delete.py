from os import system
from platform import system as sys

class delete:
    def __init__(self):
        self.run()
        # Call the run function
    def run(self):
        """
        Make a confirm to del the website and del it.
        """

        qes = input("\033[0;32mConfirm (Y/N):\033[m").upper()
        
        if qes == "Y":
            if sys() == "Linux":
                system('rm -R app/')
            elif sys() == "Windows":
                system('RD /S app/')
        else:
            print('\033[0;35mGoodbye\033[m')
