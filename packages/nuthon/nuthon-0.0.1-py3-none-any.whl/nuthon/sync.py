from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
from weakref import WeakValueDictionary
from pathlib import Path

from nuthon.resource import resource
#WILL DELETE THIS FILE EVENTUALLY.


# Integrer l'objectif de cette class directement dans 'folder'
class NuthonFileSystemEventHandler(FileSystemEventHandler):
    
    def __init__(self):
        super().__init__()
        self.resources = WeakValueDictionary()

    def sync(self, res):
        assert isinstance(res, resource), f"{type} not a res"
        self.resources[res.__path__] = res

    def dispatch(self, event):
        path = Path(event.src_path)
        if path in self.resources.keys():
            res = self.resources[path]
            if event.event_type == 'modified':
                print ("~", res)
                print ("\tWILL CALL res.__update__ ?")
                # might be usefull to know when the update
                # have finished..
            else:
                print ("\nUPDATING:\t", res, event.event_type)
        else:
            if event.event_type == 'deleted':
                print ("-", event.src_path)
            elif event.event_type == 'created':
                print ("+", event.src_path)
            elif event.event_type == 'closed':
                pass #print (")", event.src_path)
            elif event.event_type == 'modified':
                pass #print ("~", event.src_path)
            elif event.event_type == 'moved':
                #print ("MOVED: ", event)
                pass
            else:
                print ("\nRECEVIED:\t", path in self.resources.keys(), event.src_path, dict(self.resources), type(event), event.event_type, type(event.event_type))
            

# might be better to instantiate handler
# for each resource sync request ?
handler = NuthonFileSystemEventHandler()
guard = Observer()
guard.schedule(handler, Path('.').resolve(), recursive=True)

def sleep():
    import time
    time.sleep(0.1)
    handler.tick()
    
def loop(fun=sleep):
    guard.start()
    try:
      while True:
        fun()
    except KeyboardInterrupt:
        guard.stop()
    guard.join()
    return guard
