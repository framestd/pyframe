from __future__ import print_function
import os
import time
import sys
msg = "{} is missing -- sledge {} continue without {}"
cprint = lambda m, c: print(m)
if os.name == 'nt':
    try:
        import colorama
        colorama.init()
    except ImportError:
        print(msg.format("colorama", "will", "all those fancy colors"))
try:
    from termcolor import cprint
except ImportError:
    print(msg.format("termcolor", "will", "all those fancy colors"))

def log(*msgs):
    print(*msgs)
def error(msg):
    cprint("error: {}".format(msg), "red")
    time.sleep(1.0)
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')
def warn(msg):
    cprint("warning: {}".format(msg), "yellow")
    time.sleep(0.75)
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')
def info(msg):
    cprint(msg, "blue", attrs=["bold"])
    time.sleep(0.5)
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')
def success(msg):
    cprint("success: {}".format(msg), "green")
def aware(msg):
    cprint(msg, "cyan")
def sledge(msg, *args):
    cprint(msg, *args)