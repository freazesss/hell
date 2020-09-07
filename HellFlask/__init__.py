from .HellOptions import HellOptions 


class HellFlask:
    def __init__(self, option: str, name: str=""):
        self.option = option
        self.name = name
        self.HellOpts = HellOptions()
        self.verify()

    def verify(self):
        if self.option == "::create":
            self.HellOpts.create(self.name)
        elif self.option == "::run":
            self.HellOpts.run()
        else:
            print("Invalid option.")