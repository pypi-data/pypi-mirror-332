from pathlib import Path
from sys import stdout
from . import log

from argparse import ArgumentParser
ap = ArgumentParser()

ap.add_argument("path", nargs='?',
        help="relative or absolute path of the entity.")

opt, remainin = ap.parse_known_args()

if opt.path is None:
    log("Path is not defined, using current folder as "
        "the entity.")
    opt.path = '.'
opt.path = Path(opt.path)
# Path asserted

from .active_context import entity_context
with entity_context(opt.path) as entity:
    try:
        from time import sleep
        print ("\n\nEntity process control:\n\tUse CTRL-C !")
        while not hasattr(entity, 'error'):
            # When to auto stop ?
            sleep(0.1)
            #print (".", end="")
            stdout.flush()
    except KeyboardInterrupt:
        print ("Entity runtime stopped by ctrl-C.")
        
# Entity activated, used, desactivated
