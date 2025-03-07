from functools import partial
log = partial(print, "[e]\t")

import sys
sys.path.append('..')
import nuthon
from traceback import format_exception_only, format_stack
def excepthook(typ, value, tb):
    while tb:
        f_code = tb.tb_frame.f_code
        hidden = '__notrace__' in f_code.co_varnames
        frozen = f_code.co_filename == '<frozen runpy>'
        if hidden: pass
        elif frozen: pass
        for l in format_stack(tb.tb_frame, 1):
            l = l.replace("  File ", "--------> ")
            l = l.replace("\n    ", "\n ")
            print ("-nu" if hidden else "-py" if frozen else "---", end="")
            print (l, end="")
        tb = tb.tb_next
    # Traceback done
    for line in format_exception_only(value):
        print (line)
    # Exception description done
old_sys_excepthook = sys.excepthook
sys.excepthook = excepthook
