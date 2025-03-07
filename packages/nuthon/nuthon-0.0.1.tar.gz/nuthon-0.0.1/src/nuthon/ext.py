from pathlib import Path
from collections import OrderedDict
from nuthon.common import strong
from nuthon.abstract import abstract
from nuthon.resource import resource

class ExtensionError(Exception):
    pass

index = OrderedDict()
def extension(self):
    if not self.__name__ in index:
        index[self.__name__] = self
        return self
    else:
        return index[self.__name__]

def infer(key):
    assert isinstance(key, str)
    for k in index.keys():
        yield key + '.' + k

def quick_bundle(*args, key=None, create=False):
    __notrace__ = True
    if len(args) == 0:
        if key is None: return None
        ikeys = infer(key)
        for ikey in ikeys:
          if ikey in index.keys():
            assert False, ("WORK TODO", ikey)
          else:
            assert False, ("Not impemented ?", ikey)
    elif len(args) == 1:
        return single_bundle(args[0], key, create=create)
    elif len(args) >= 2:
        print ("WHAT?", args)
        raise NotImplementedError("yeah...")
    else:
        assert False, (args, key, create)
    return single_bundle(args[0], key, create=create)

def single_bundle(path, key, create=False):
    from .folder import folder
    __notrace__ = True
    x = path.suffix if not str(path.name).startswith('.') else path.name
    from pathlib import Path
    y = path.name.replace(x, '').replace(Path(path.stem).suffix, '')
    x = x[1:] if x.startswith('.') else x
    y = '' if y == key else y
    resource_type = folder if path.is_dir() else resource
    if x in index.keys():
        resource_type = resource_type-index[x]
    elif path.is_dir():
        pass # loading a folder
    elif create and not '.' in key:
        pass # creating single file
    elif path.exists():
        pass # the file already exists
    elif not path.exists() and x in [None, '']:
        pass # do not create files with empty name
    elif not path.exists() and not create:
        assert False, f"The requested resource ({path}) does not exists and cannot be created."
    else:
        print (index.keys(), path, key, y)
        print (f"I'f you're here, you're not where you should be looking... stating on; {x}")
        raise ExtensionError(f"No extension for '{x}' ({path}) {list(index.keys())} {key} ?? {y}\n.")
    return resource_type(path, create=create)

class ext(abstract):
    __slots__ = ()
    def __ascend__(self, path):
        return path.read_text()

    def __descend__(self, txt):
        self.__path__.write_text(txt)

    @strong
    def __init__(self, path, create=False, **kwargs):
        super().__init__()
        path = path if isinstance(path, Path) else Path(path).absolute()
        self.__core__ = self.__ascend__(path=path)
        assert self.__core__, (path, self.__core__, self.__ascend__)
        
    def __str__(self):
        try:
            return f"<{type(self)}({type(self.__core__).__name__})@{self.__path__}>"
        except RecursionError:
            return "recursion-error"
    def __getattr__(self, key):
        raise Exception(f"{type(self).__name__}.__getattr__ not implemented")
    def __getx__(self, key):
        raise Exception(f"{type(self).__name__}.__getx__ not implemented")
    def __setx__(self, key, value):
        raise Exception(f"{type(self).__name__}.__setx__ not implemented")    
    def __normalize__(self, value, key=None):
        raise Exception(f"{type(self).__name__}.__normalize__ not implemented")
    def __update__(self):
        raise Exception(f"{type(self).__name__}.__update__ not implemented")

