from . import create
from . import delete
from . import run

class Hell:
    def __init__(self):
        self.run()
    def run(self):
        asincart = """
      ___ ___         .__  .__   
    /   |   \   ____ |  | |  |  
    /    ~    \_/ __ \|  | |  |  
    \    Y    /\  ___/|  |_|  |__
    \___|_  /  \___  >____/____/
    \/       \/           
        """
        print(f"""\033[0;31m{asincart}\033[m""")
        print("\033[0;32m> Tool to create Flask websites\033[m")

        try:
            self.question = input("\033[0;33m[1] Create app\n[2] Delete app\n[3] Run app\033[m\n\n\033[0;35mType it:\033[m")
            self.commands()
        except KeyboardInterrupt:
            return 
    def commands(self):
        if self.question == "1":
            create.create()
            print("\033[0;36mYour app has been created.\033[m")
        elif self.question == "2":
            delete.delete()
            print("\033[0;34mYour app has been deleted.\033[m")
        elif self.question == "3":
            print("\033[0;31mYour app has been started.\033[m")
            run.run()