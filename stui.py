class CommandOptions:
    def __init__(self, title=""):
        self.title = title
        self.options = {}

    def add(self, key, name, callback):
        self.options[key] = (name, callback)
    
    def ask(self, run=False):
        if self.title != "": print(f"{self.title}:")
        for k in self.options:
            print(f"\t[{k}] {self.options[k][0]}")
        c = ""
        while c == "":
            c = input("> ")
            if c in self.options.keys():
                if run and self.options[c][1] != None: self.options[c][1]()
                return c
            else:
                c = ""

class ChoiceOptions(CommandOptions):
    def __init__(self, title=""):
        self.title = title
        self.options = {}
        self.count = 0

    def add(self, name, callback):
        self.options[str(self.count)] = (name, callback)
        self.count += 1