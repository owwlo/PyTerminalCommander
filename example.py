
from collections import deque
from threading import Thread

import urwid
import threading
import sys
import os
import traceback
import time

from PyTerminalCommander import Commander, CommandHandler, CommanderPopupLauncher

if __name__=='__main__':
    # Define the handler
    class CommandSet(CommandHandler):
        def do_echo(self, commander, extra):
            '''echo - Echo all arguments'''
            return extra

        def do_raise(self, commander, extra):
            '''Raise an exception'''
            raise Exception('Some Error')

        def do_quit(self, *args):
            '''Exit the program.'''
            return Commander.Exit

        def do_yellow(self, commander, extra):
            '''Output the following text in yellow.'''
            return (extra, "yellow")

        def do_green(self, commander, extra):
            '''Output the following text in green.'''
            time.sleep(10)
            return (extra, "light_green")

        def do_notify(self, commander, extra):
            '''Show a notification popup.'''
            commander.notify(
                ["This is a ", ("yellow", "notification: "), extra, "."],
                CommanderPopupLauncher.DEFAULT_DURATION
            )

    c = Commander('This is the title of the frame'
        , cmd_cb = CommandSet()
        , hook_stdout = True
        , hook_stderr = True
        , show_help_on_start = True
        , show_line_num = True
        , extra_pallete = [
            ('light_green', urwid.LIGHT_GREEN, urwid.BLACK),
            ('yellow', urwid.YELLOW, urwid.DARK_BLUE),
        ]
    )

    # Print things from another thread
    import time
    def run():
        while True:
            time.sleep(1)
            c.output('Tick')
    t = Thread(target = run)
    t.daemon=True
    t.start()

    c.loop()
