from abc import ABCMeta

index = dict()

class meta(ABCMeta):
    def __repr__(self):
        return f"#{self.__name__}#"
    
    def __str__(self):
        return f"#{self.__name__}"

    def __init__(self, name, bases, body):
        super().__init__(name, bases, body)
        assert hasattr(self, '__slots__'), 'no slots ???'

# extension interface
    def __sub__(self, other):
        if not self in index.keys():
            index[self] = dict()
        if other in index[self]:
            return index[self][other]
        from .common import resolve
        body = resolve(self, other,
                       __call__=True,
                       __init__=True,
                       __new__=True)
        name = f"{self.__name__}-{other.__name__}"
        x = type(name, (self, other), body)
        index[self][other] = x
        return x
