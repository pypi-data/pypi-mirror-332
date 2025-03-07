from pathlib import Path

class entity_context:
    def __init__(self, path):
        self.path = Path(path).absolute().resolve()
        assert not (self.path / '__init__.py').exists(), f"{self.path} already running"

    def __enter__(self):
        print ("Entering context of entity", self.path)

        assert not (self.path / '__init__.py').exists()
        
        from nuthon.ext import single_bundle
        entity = single_bundle(self.path, key="entity")
        # folder (entity) ----------------------------

        from nuthon.json import json
        e_json = single_bundle(self.path / '.json',
                               'json', create=True)        
        entity.__core__ = e_json
        # json (data) -----------------------------

        from os import getcwd
        cwd = getcwd()
        # imitating this environ

        from nuthon.py import py
        e_init = single_bundle(self.path / '__init__.py',
                               'init', create=True)
        e_init.__descend__(f"""# This file is auto-generated and auto-removed. Any edit is useless and will be lost at exit.
# See nuthon/Entity/active_context.py to alter
from sys import path
from pathlib import Path
path.append("{cwd}")
path.append("{Path(cwd).parent}")
import nuthon.json
import nuthon.py
from nuthon.ext import single_bundle
self = single_bundle(Path("{self.path.absolute()}"), key="{self.path}")
__all__ = ("self", )
        """)
        # init (python module) -------------------------------
        return entity
        
    def __exit__(self, typ=None, value=None, traceback=None):
        print ("Exiting context of entity", self.path)
        
        from os import remove as remove_file
        remove_file (self.path / '__init__.py')
         # remove the __init__ anyway

        if typ is None: return # no exception.
        value.add_note(f"This exception occured in the context of entity {self}")
