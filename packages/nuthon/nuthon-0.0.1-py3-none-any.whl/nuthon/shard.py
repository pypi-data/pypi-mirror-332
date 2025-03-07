from collections.abc import MutableMapping, MutableSequence
from nuthon.abstract import abstract


class shard(abstract):
    __slots__ = ('__parent__', '__data__', '__fresh__')
    
    def __enter__(self):
        assert self.__fresh__, self
        self.__fresh__ = False
        
    def __exit__(self, typ=None, value=None, traceback=None):
        assert not self.__fresh__
        self.__fresh__ = True

    def __update__(self):
        __notrace__ = True
        if self.__fresh__:
            self.__parent__.__update__()
        
    def __init__(self, parent):
        self.__fresh__ = False
        self.__parent__ = parent
        self.__data__ = self.__default__()
        self.__fresh__ = True

    def __len__(self):
        return len(self.__data__)
    def __iter__(self):
        return iter(self.__data__)

    def __setattr__(self, key, value):
        __notrace__ = True
        if key == '__fresh__':
            assert isinstance(value, bool), type(value)
            return object.__setattr__(self, key, value)
        if key == '__parent__':
            from nuthon.ext import ext
            assert isinstance(value, ext), type(value)
            return object.__setattr__(self, key, value)
        elif key == '__data__':
            assert isinstance(value, (MutableMapping, MutableSequence)), type(value)
            return object.__setattr__(self, key, value)
        self.__data__[key] = self.__normalize__(value)
        self.__update__()

    def __normalize__(self, value, key=None):
        return self.__parent__.__normalize__(value, key=key)

    def __serialize__(self):
        raise Exception(f"{type(self).__name__}.__serialize__ not implemented")
    def __default__(self):
        raise Exception(f"{type(self).__name__}.__default__ not implemented")

    def __str__(self):
        return f"[{self.__data__}{self.__parent__}]"
    def __repr__(self):
        return f"{self.__class__}"

class list_shard(shard, MutableSequence):
    def __default__(self):
        return []
    def insert(self, value, at):
        self.__data__.insert(value, at)
        self.__update__()
    def __init__(self, parent, *values):
        super().__init__(parent)
        with self:
            for x in values:
                self.append(x)

    def __delattr__(self, key):
        assert isinstance(key, int), (type(key), key)
        if len(self.__data__) > key:
            del self.__data__[key]
            assert not key in self.__data__, key
            self.__update__()
        else:
            raise AttributeError(f"{key} does not exists on {self}")
        

    def __getattr__(self, key):
        assert isinstance(key, int), (type(key), key)
        if len(self.__data__) > key:
            return self.__data__[key]
        raise AttributeError(f"{key} does not exists on list-shard")
            
    def __serialize__(self):
        return [
            value if isinstance(value, (str, int, float))
            else "ø" if value is None 
            else self.__normalize__(value) if isinstance(value, (list, tuple, dict))
            else value.__serialize__()
            for value in self.__data__
        ]

class dict_shard(shard, MutableMapping):
    def __default__(self):
        return {}
    def __init__(self, parent, **values):
        super().__init__(parent)
        with self:
            for k, v in values.items():
                self[k] = v    

    def __delattr__(self, key):
        if key.startswith('__'):
            raise AttributeError(f"{key} does not exists on dict-shard")
        elif key in self.__data__.keys():
            del self.__data__[key]
            assert not key in self.__data__, key
            self.__update__()
        else:
            raise AttributeError(f"{key} does not exists on {self}")
        

    def __getattr__(self, key):
        if key.startswith('__'):
            raise AttributeError(f"{key} does not exists on dict-shard")
        if key in self.__data__.keys():
            return self.__data__[key]
        raise AttributeError(f"{key} does not exists on {self}")
            
    def __serialize__(self):
        return {
            key: value if isinstance(value, (str, int, float))
            else "ø" if value is None
            else self.__normalize__(value) if isinstance(value, (list, tuple, dict))
            else value.__serialize__()
            for key, value in self.__data__.items()
        }
