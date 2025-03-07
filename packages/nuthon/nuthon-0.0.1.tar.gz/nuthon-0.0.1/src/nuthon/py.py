from nuthon.ext import ext, extension

@extension
class py(ext):
#    __slots__ = ("__ext_instance__",)
# This is not possible to add __slots__ in any descendant
# of ext class (because it create on-the-fly class mixin)
    
    def __ascend__(self, path):
        def lazy_py_compiler():
            source = ext.__ascend__(self, path)
            return compile(source, path, 'exec')
        return lazy_py_compiler
    
    def __call__(self, *args, **kwargs):
        from kathon.yl import yl
        if self.__bind__ is None:
            context = yl(args=args, **kwargs) * self
        else:
            context = yl(self=self.__bind__,
                         args=args, **kwargs) * self
        if 'result' in context:
            return context.result

    def __lshift__(self, folder):
        self.__bind__ = folder
