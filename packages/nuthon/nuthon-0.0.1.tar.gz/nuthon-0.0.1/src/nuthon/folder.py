from collections.abc import Sequence
from pathlib import Path
from nuthon.resource import resource, index
from nuthon.common import weak, strong, NoCreationError
from nuthon.tag import is_script

# access file in the folder with
#> folder_reference / namefile_str

# access variable in the .json file with
#> folder_reference.field_name




class folder(resource, Sequence):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if (self.__path__ / '.json').exists():
            self.__core__ = self['.json']

    def __iter__(self):
        for x in self.__path__.glob('*'):
            yield x

    def __len__(self):
        return len(tuple(self.__path__.glob('*')))

    def __create__(self, *args, create=False, key=None, **kw):
        __notrace__ = True
        #print ("folder.py(__create__):", args, kw)
        if len(args) == 1 and key is None:
            arg = args[0]
            if arg.endswith('.json') or arg.endswith('.py'):
                new = resource.__create__(self, arg,
                                create=True, **kw)
            else:
                arg = arg.extension('.py')
                new = resource.__create__(self, arg,
                                create=True, **kw)       
            return new
        return resource.__create__(self, *args, create=create,
                                   key=key, **kw)
    def _creation_error(self, method_name, *args, **kwargs):
        if not self.__core__ is None:
            if method_name == '__setattr__':
                self.__core__[args[0]] = args[1]
            elif method_name == '__getattr__':
                return self.__core__[args[0]]
            else:
                assert False, f"{method_name} has no defined recovery"
        else:
            assert False, f"{self} has no core"

        
    def __setattr__(self, key, value):
        try:
            resource.__setattr__(self, key, value)
        except AttributeError:
            try:
                assert not Path(key).exists(), key
                x = self[key]
            except NoCreationError:
                return self._creation_error('__setattr__',
                                            key, value)
            if hasattr(x, '__descend__'):
                x.__descend__(value)
            else:
                __notrace__ = True
                raise

    def __getattr__(self, key):
        __notrace__ = True
        if isinstance(key, str):
            if key.startswith("__") and key.endswith("__"):
                x = resource.__getattr__(self, key)
                if x is not None: return x
                # It's already not found on the python system
                # Better to raise AdequateErrors
                assert False, "Here lies dragons"
        else: return self.__create__(key, key=None)
        y = []
        path = self.__path__ / key
        if path.exists():
            y.append(path)
        from .ext import infer
        for k in infer(key):
            x = self.__path__ / k
            if x.exists():
                y.append(x)
        z = []
        for p in y:
            if str(p) in index:
                z.append(index[str(p)])
        assert len(z) <= 1, (key, z)
        if len(z) == 1:
            return z[0]
        try:
            x = self.__create__(*y, key=key)
            if is_script(x): x << self
            return x
        except NoCreationError:
            return self._creation_error('__getattr__', key)
    # is used by __add__, __sub__

    # operators interface
    def __call__(self, arg=None, **kwargs):
        from kathon.yl import yl
        return yl(self=self, arg=arg, **kwargs) * self['.py']
    # call this folder hidden script, the env is refreshed
    # every call
    #        - arg --> give something more in the env
    #        - kwargs --> define variable in the env
    
    def __sub__(self, path):
        __notrace__ = True
        return getattr(self, str(path))
    # is used by __add__
    #equivalent to folder.path#
    def __add__(self, path):
        __notrace__ = True
        if isinstance(path, type):
            path = path.__name__
        if not (self.__path__/path).exists():
            return self.__sub__(path)
        else: return getattr(self, path)
    # use __sub__ to try to create the file
    # if it doesn't exists (using -c)
    #equivalent to folder.path#
    
    # testing file presence with:
    #    some_folder / 'some_filename.txt'
    def __truediv__(self, other):
        if isinstance(other, str):
            return (self.__path__ / other).exists()
        assert False, f"Unknow operand for {type(self).__name__}: {type(other)}"

    # creating file with:
    #    some_folder * {"somefile.txt": "some text"}
    #                 or:
    #    some_folder * "{some_folder.__path__}/somefile.txt"
    def __mul__(self, other):
        if isinstance(other, dict):#  This is a bit ugly...
         for k, v in other.items(): # not very good sugar..
          if hasattr(v, 'core'):
             v = v.core
          if hasattr(v, '__core__'):
             v = v.__core__
    # extract the core is not a dict or string         
          if hasattr(v, '_MutableMapping__marker'):
             from futhon.shard import shard
             assert isinstance(v, shard), type(v).__module__
             v = v.__serialize__()
    # transform the core into a dict or string
          if isinstance(v, dict) and not "." in k:
            f = self.__class__(self.__path__ / k, create=True)
            f * v
            return f
          elif isinstance(v, dict):
            f = self.__create__((self.__path__ / k), key=k, create=True)
            f.__descend__(v)
            return f
          elif isinstance(v, str):
            import futhon.json
            f = self.__create__((self.__path__ / k).with_suffix('.json'), key=k, create=True)
            f.value = v
            return f
          elif isinstance(v, list):
              self[k] = v
              assert False, [type(v), self.__path__, v, k]
          else: assert False, [type(v), dir(v), v, k]
    # writing depending on type          
        elif isinstance(other, str):
            assert other.startswith(str(self.__path__))
            return self.__create__(Path(other), create=True)
    # plain file writing
        else: assert isinstance(other, dict), type(other)
    
    @strong
    def __new__(cls, arg, create=False):
        if isinstance(arg, Path):
            path = arg
        elif isinstance(arg, str):
            path = Path(arg)
        else:
            assert False, type(arg)
        if not path.exists():
            if create:
                path.mkdir(parents=True)
            else:
              raise AttributeError(f"{path.absolute()} does not exists")
        return resource.__new__(cls, path)
