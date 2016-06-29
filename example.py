
from collections import deque
from threading import Thread

import urwid
import threading
import sys
import os
import traceback

from PyTerminalCommander import Commander, CommandHandler

if __name__=='__main__':

    # Print things from another thread
    import time
    def run():
        while True:
            time.sleep(1)
            print('Tick')
    t = Thread(target = run)
    t.daemon=True
    t.start()

    # Define the handler
    class CommandSet(CommandHandler):
        def do_echo(self, commander, extra):
            '''echo - Just echos all arguments'''
            return extra

        def do_raise(self, commander, extra):
            raise Exception('Some Error')

        def do_quit(self, *args):
            return Commander.Exit

        def do_yellow(self, commander, extra):
            return (extra, "yellow")

        def do_green(self, commander, extra):
            return (extra, "light_green")

    c = Commander('This is the title of the frame'
        , cmd_cb = CommandSet()
        , hook_stdout = True
        , hook_stderr = True
        , show_help_on_start = True
        , show_line_num = True
        , extra_pallete = [
            ('light_green', urwid.LIGHT_GREEN, urwid.BLACK),
        ]
    )
    c.loop()
