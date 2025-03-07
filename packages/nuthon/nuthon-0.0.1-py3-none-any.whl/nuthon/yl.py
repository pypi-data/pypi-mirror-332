from collections.abc import MutableMapping, Sequence
from inspect import iscode
from nuthon.meta import meta
from nuthon.common import strong

# REDO INTO ctx
#    also create contextualized-abstract
#    with __get__(self, instance, owner)
#    and  __set__(self, instance, value)
#         (do not use return in this context...)
#
#   get -> contextualize with the instance/owner
#
#   set -> raise errors and swap entities with value
#
#   also beware of the __getattribute__ that might have
# blocked this effect on global/local scope
class yl(dict, metaclass=meta):
    __slots__ = ('__proxy__', )
    # slots aren's useless since dict object has no __dict__

    # scope interface (to be implemented in a subclass only)
    def __enter__(self): 
        proxy = yl()
        proxy.__proxy__ = self
        return proxy
    def __exit__(self, typ=None, value=None, traceback=None):
        if typ is None: return
        # should not raise here

    # execution interface (another subclass ?? not sure...)
    def __mul__(self, other):
        if hasattr(other, '__core__'):
            code = other.__core__
            entity = other
        elif iscode(other):
            code = other
        else: raise TypeError(f"{type(self)} Can't execute {type(other).__name__} from {other}")
        # end type recon
        if isinstance(code, SyntaxError):
            raise code
        elif callable(code):
            code = code()
        # start exec
        if code:
            try:
                exec (code, self, self)
            except Exception as e:
              __notrace__ = True
              raise e.with_traceback(e.__traceback__.tb_next)
        return self
        
    # dict interface (alter this at last)
    def __setitem__(self, key, value):
        # this is where I intervene...
        key = str(key)
        if key.startswith('__'):
            if hasattr(self, '__set__'):
                self.__set__(key, value)
            else:
                __notrace__ = True
                raise AttributeError(f"Can't set {type(self)}.{key} = {type(value).__name__}")
        else:
            dict.__setitem__(self, key, value)
    def __getitem__(self, key):
        if isinstance(key, int): # accessing value by order
            return list(self)[key]
        # This is ugly as shit........
        key = str(key)
        if key == '__builtins__':
            from lithon.common import __builtins__
            return __builtins__
        if hasattr(self, '__proxy__'):
            try:
                return self.__proxy__.__getitem__(key)
            except KeyError:
                pass
        return dict.__getitem__(self, key)
    def __delitem__(self, key):
        key = str(key)
        assert not key.startswith('__'), key
        dict.__delitem__(self, key)
    def __iter__(self):
        return (k for k in dict.keys(self) if not k.startswith('__'))
    
    # functional interface
    def __contains__(self, key):
        if hasattr(self, key): return True
        if hasattr(self, '__proxy__'):
            return key in self.__proxy__
    def __setattr__(self, key, value):
        if key.startswith("__"):
            return dict.__setattr__(self, key, value)
        self[key] = value
    def __getattribute__(self, key):
        if key.startswith("__") or key in ('keys', 'clear', 'copy', 'dump', 'fromkeys', 'get', 'items', 'pop', 'popitem', 'setdefault', 'update', 'values'):
            return dict.__getattribute__(self, key)
        if key in dict.keys(self):
            return self[key]
        if hasattr(self, '__proxy__'):
            return getattr(self.__proxy__, key)
        __notrace__ = True
        raise AttributeError(f"{key} does not exists on {type(self)}")
    def __delattr__(self, key):
        if key.startswith("__"):
            return dict.__delattr__(self, key)
        del self[key]

    def __iter__(self):
        return dict.__iter__(self)
    
    # textual interface    
    def __str__(self):
        return f"<[{self.__class__.__name__}] {tuple(iter(self))}>"
    def __repr__(self):
        return f"<{self.__class__.__name__}>"

    # meta interface
    @classmethod
    def dump(self, level=0):
        print (" ." * level + ' ' + self.__name__)
        level += 1
        for m in self.index:
            assert not m is self
            m.dump(level)

