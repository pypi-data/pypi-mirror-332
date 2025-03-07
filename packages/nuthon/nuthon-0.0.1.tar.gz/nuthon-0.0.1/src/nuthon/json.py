from json import loads
from collections.abc import Mapping, Sequence
from nuthon.ext import ext, extension
from nuthon.shard import dict_shard, list_shard, shard

@extension
class json(ext):
    default = "{}"
    
    def __ascend__(self, path):
        def lazy_json_reader():
            txt = ext.__ascend__(self, path)
            txt = self.default if txt == "" else txt
            data = loads(txt)
            if isinstance(data, dict):
                self.__core__ = dict_shard(self, **data)
            elif isinstance(_data, (list, tuple)):
                self.__core__ = list_shard(self, **data)
            else:
                assert False, type(data)
            return self.__core__
        return lazy_json_reader

    def __update__(self):
        __notrace__ = True
        if not isinstance(self.__core__, shard):
            assert False, "unexpcted update"
        self.__descend__(self.__core__)

    def __delattr__(self, key):
        delattr(self.__core__, key)

    def __descend__(self, data):
        __notrace__ = True
        from json import dumps
        serial = data.__serialize__() if not isinstance(data, dict) else data
        if isinstance(serial, json):
            serial = serial.__ascend__(serial.__path__)
        if isinstance(serial, shard):
            serial = serial.__serialize__()
        if serial == "":
            serial = "{}"
        try:
            data = dumps(serial)
        except TypeError as e:
            print ("\n\n!!\t", e)
            print ("serial=", type(serial), "\n",
                   "data=", type(data), "\n",
                   isinstance(serial, json))
            input("json.py")
            raise e
        super().__descend__(data)

    def __normalize__(self, value, key=None):
        if isinstance(value, (str, int)):
            return value
        elif isinstance(value, Mapping):
            return dict_shard(self, **value)
        elif isinstance(value, Sequence):
            return list_shard(self, *value)
        elif hasattr(value, '_to_json'):
            return value._to_json(key=key)
        assert False, type(value)

    def __getx__(self, key, what=None):
        if not isinstance(self.__core__, shard):
            return self.__core__()[key]
        return self.__core__[key]
        
    def __setx__(self, key, value):
        __notrace__ = True
        if not isinstance(self.__core__, shard):
            self.__core__()[key] = value
        else:
            self.__core__[key] = value
        self.__update__()
