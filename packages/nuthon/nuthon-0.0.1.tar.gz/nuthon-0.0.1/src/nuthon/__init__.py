try:
 from startup import options
except ModuleNotFoundError:
 from nuthon.startup import options
except BaseException as e:
 raise e

from pathlib import Path

nuthon_folder=Path(__file__).parent
print ("NUTHON FOLDER=", nuthon_folder)

# Inferring the folder of this nuthon module.
from nuthon import nuthon_folder
from pathlib import Path
def relative_to_nuthon(s, folder=nuthon_folder):
 return s.replace(str(folder) + '/', "nuthon@")

from argparse import ArgumentParser
ap = ArgumentParser()

ap.add_argument("--no-excepthook", action='store_true',
        help="before exiting, will watch for change"
        " in the path and might react to it")
ap.add_argument("--debug", action='store_true',
        help="Show nuthon hidden stack in exception"
        " traceback and show debug log from nuthon"
        "modules, such as resource.py, folder.py")
opt, remaining = ap.parse_known_args()


import sys
from traceback import format_exception_only, format_stack
def excepthook(typ, value, tb):
    print ('\nCongratulation !!\nYou broke nuthon, enjoy the traceback:\nYou can use:\n\t --debug to include nuthon\'s hidden calls.\n\t --silent to remove warning from the output.\n')
    print (sys.path)
    while tb:
        f_code = tb.tb_frame.f_code
        hidden = '__notrace__' in f_code.co_varnames
        frozen = f_code.co_filename == '<frozen runpy>'
        if not opt.debug and hidden: pass
        elif not opt.debug and frozen: pass
        else:
            for l in format_stack(tb.tb_frame, 1):
                l = relative_to_nuthon(l)
                l = l.replace("  File ", "--------> ")
                l = l.replace("\n    ", f"\n ")
                print("" if not opt.debug else "-nu" if hidden else "-py" if frozen else "---", end="")
                print (l, end="")
            if not (opt.debug and frozen): print()
        tb = tb.tb_next
    # formated traceback
    for line in format_exception_only(value):
        print (line)
old_sys_excepthook = sys.excepthook
if not opt.no_excepthook:
    sys.excepthook = excepthook
# exception
