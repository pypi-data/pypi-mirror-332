from nuthon.common import weak
from nuthon.meta import meta

class abstract(metaclass=meta):
    __slots__ = ('__weakref__', )

    # create
    @weak
    def __call__(self, *args, **kwargs):
        __notrace__ = True
        raise Exception(f"undefined __call__ in {type(self)}")
    # ???

    
    # str
    def __str__(self):
        try:
            return f"{type(self)}@{repr(self)}#"
        except:
            return "broken-abstract"
    def __repr__(self):
        raise Exception(f"undefined __repr__ in {type(self)}")


    # Add __xset__, __xget__, __xdel__
    # so both __*attr__ and __*item__
    # can fallback on it
    #    ( this will be usefull for yl -> ctx )

    # set
    def __setattr__(self, key, value):
        if key == '__weakref__':
            return object.__setattr__(self, key, value)
        raise Exception(f"undefined __setattr__ in {type(self).__name__} class")
    def __setitem__(self, key, value):
        __notrace__ = True
        return self.__setattr__(key, value)

    # get
    # __getattrbute__ not altered ??
    def __getattr__(self, key):
        raise Exception(f"undefined __getattr__ in {type(self).__name__} class")
    def __getitem__(self, key):
        __notrace__ = True
        return self.__getattr__(key)

    # del
    def __delattr__(self, key):
        raise Exception(f"undefined __delattr__ in {type(self).__name__} class")
    def __delitem__(self, key):
        return self.__delattr__(key)
