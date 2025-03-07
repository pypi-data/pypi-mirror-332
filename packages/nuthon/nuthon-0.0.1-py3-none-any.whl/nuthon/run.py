from sys import executable, stdout
from subprocess import Popen
from time import sleep
from pathlib import Path

MODES = dict(ENTITY=-1)

folder = Path(__file__).parent
from os import chdir, getcwd

procs = []

def run(path=".", mode=-1):
    # mode:
    # -1        ->    Daemon (do not exit by itself)
    # 
    path = Path(path).absolute()
    if mode == -1:
        old_dir = getcwd()
        chdir(folder)
    # pathing

    if mode == -1:
        x = Popen([executable, "-m", "Entity", path],
                  shell=False)
        print ("run_all.py(RUN):", type(x), x)
    else:
        assert False, "Unknown mode %s" % mode
    # processing

    print (f"RUN -> {path}")
    procs.append(x)
    # registering
    
    sleep(0.1)
    # Waiting a bit in the main process for the child process
    # to populate the target folder with __init__.py

# TODO: make a 'with' object to prevent unexpected cwd change.
    if mode == -1:
        chdir(old_dir)
    # path closing
    return x

def join():
    if len(procs) > 0:
        procs[0].wait()

def finish(sleep_time=0.1):
    from time import sleep
    while len(procs) > 0:
        print (f"Start waiting for processes ({len(procs)})"
           " to finish.")
        try:
            while len(procs) > 0:
                stdout.flush()
                x = procs[0]
                i,o = x.communicate()
                if i or o:
                    print ("nuthon/run.py", i, o)
                sleep(sleep_time)
                x.wait()
                print ("Process done: ", *x.args)
                procs.pop(0)
        except KeyboardInterrupt:
            print ("Forcefull exit of :")
            for x in procs:
                print (">\t", *x.args)
                stdout.flush()
                x.wait()
