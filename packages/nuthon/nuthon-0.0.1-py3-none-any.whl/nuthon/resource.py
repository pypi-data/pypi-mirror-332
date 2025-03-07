from nuthon.common import weak, strong, create_reflector, NoCreationError
from collections.abc import Mapping, Sequence, Callable
from pathlib import Path
from nuthon.abstract import abstract

thindex = {}

index = {} #was yl()
class resource(abstract):
    __slots__ = ('__core__', '__path__', '__bind__')

    # text interface
    def __repr__(self):
        return str(self.__path__)

    # attribute interface
    def __setattr__(self, key, value):
        __notrace__ = True
        if key == '__bind__':
            object.__setattr__(self, key, value)
        elif key == '__path__':
            assert isinstance(value, Path)
            object.__setattr__(self, key, value)
        elif key.startswith('__ext_') and key.endswith('__'):
            object.__setattr__(self, key, value)
        elif key == '__core__':
            assert isinstance(value, (type(None),
                                      Mapping,
                                      Sequence,
                                      Callable)), type(value)
            object.__setattr__(self, key, value)
        elif hasattr(self, '__setx__'):
            self.__setx__(key, value)
        elif not key.startswith('__'):
            if self.__core__:
                self.__core__.__setattr__(key, value)
            else:
                raise AttributeError(key)
        else:
            abstract.__setattr__(self, key, value)
    
        # AttributeInterface
    def __getattr__(self, key):
        __notrace__ = True
        if isinstance(key, int):
            #if (self.__path__ / (str(key)+'.json')).exists():
            #    return self[self.__path__ / (str(key)+'.json')]
            from.import opt
            if opt.create:
                from startup import options
                options.create(self, key)
                res = self(key)
            else:
                assert False, ("I NEED TO BE ABLE TO CREATE", self, key, opt.create)
                raise AttributeError(key)
        if key.startswith('__'):
            raise AttributeError(f"{key} does not exists on {type(self)}")
        if self.__core__:
            if isinstance(self.__core__, (Mapping, Sequence)):
                try:
                    return self.__core__[key]
                except AttributeError as e:
                    t = e.__traceback__
                    while t.tb_next:
                        t = t.tb_next
                    t = t.tb_next                        
                    raise e.with_traceback(t)
        if hasattr(self, '__getx__'):
            return self.__getx__(key)
        raise AttributeError(f"{key} does not exists on {type(self)}({self.__path__})")

    # watchover interface
    def __enter__(self):
        reflector = create_reflector(self)
        resource.register_context(self, reflector)
        return reflector
    def __exit__(self, typ=None, value=None, traceback=None):
        resource.close_context(self)
        if typ is None: return
        value.add_note(f"This exception occured while watching over: {self}")
    # watchover
    def __test__(self, key, value, target):
        if key in ['src_path']:
            return self.__path__ / value == Path(target.src_path)
        if key in ['event_type']:
            return value == target.event_type
        assert False, ("Unknow test: ", key) # is this used ?
        
    @staticmethod
    def register_context(res, th):
        assert not res in thindex.keys(), "ERROR"
        thindex[res] = th
    @staticmethod
    def close_context(res):
        assert res in thindex.keys(), "ERROR"
        context = thindex[res]
        del thindex[res]
        context.stop()
        
    # class interface
    @strong
    def __new__(cls, arg, *args, create=False, **kwargs):
        if isinstance(arg, Path):
            path = arg
        else:
            path = Path(arg)
        if not path.exists():
            if create:
                path.write_text("")
            else:
              raise NoCreationError(f"{path} does not exists")
        if str(path) in index:
            r = index[path]
            r.__recalled__(*args, **kwargs)
            return r
        r = abstract.__new__(cls)
        r.__path__ = path
        r.__core__ = None
        r.__bind__ = None
        index[path] = r
        r.__created__(*args, **kwargs)
        return r

    @weak
    def __recalled__(self, *args, **kwargs):
        self.__refresh__(*args, **kwargs)
    @weak
    def __created__(self, *args, **kwargs):
        self.__refresh__(*args, **kwargs)
    @weak
    def __refresh__(self, *args, **kwargs):
        pass # unused but ussefull

    @weak # __init__ might be called multiple time for a same
    # resource. It is because a resource already created will
    # not be duplicated, but it has to go throught __new__
    # and since it's still the same class as nuthon.resource
    # it will call __init__ on it every time.
    def __init__(self, path, create=False):
        super().__init__()

    def __create__(self, *args, key=None, create=None):
        __notrace__ = True
        from .ext import quick_bundle
        if len(args) == 0 and key is not None:
            args = [(self.__path__ / key).absolute()]
        if create is None:
            create = False
            try:
                from.import opt
            except ImportError:
                pass
            else:
                create = opt.create
        else:
            create=create
        x = quick_bundle(*args, key=key, create=create)
        return x

    def __contains__(self, key):
        return hasattr(self, key)
