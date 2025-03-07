try:
    from.import Speaker
    w = Speaker()
except KeyError:
    pass
from lithon.folder import folder
resources = folder(".resources", create=True)
rs = resources()

@w.register("r", scene="start", tag="edition")
def edit(r):
    print (r)

@w.register("", scene="start", tag="creation")
def create(): # There might not be any Entity
    from blessings import Terminal
    term = Terminal()
    with term.fullscreen():
        print (term.move(0, 0) + "Hello here are the current resources:")
        for x in resources:
            print ("\t", x)
        x = input("Do you want to create a new Event ?")
        if x == "" or not (x in "YESYesyes"):
            return
        print("Provide a name: ", end='')
        x = input()
    return ResourceWrapper.create(x)



class ResourceWrapper:
    @classmethod
    def create(cls, name):
        import nuthon.json
        core = resources[f"{name}.json"]
        return cls(core)
    def __init__(self, core):
        self.core = core
