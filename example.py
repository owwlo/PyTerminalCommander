
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
    def run_tick():
        while True:
            time.sleep(1)
            c.output('Tick')
    t_tick = Thread(target = run_tick)
    t_tick.daemon=True
    t_tick.start()

    from tabulate import tabulate
    import random
    def run_fixed_table():
        idx_token = None
        while True:
            time.sleep(.4)
            table_str = tabulate([
                ["Items", "Values"],
                ["decimal", random.random()],
                ["string", "I am a {}string.".format("long " * random.randint(1, 10))]
            ], headers="firstrow", tablefmt="grid")
            idx_token = c.output(table_str, line_idx=idx_token)
    t_fixed_table = Thread(target = run_fixed_table)
    t_fixed_table.daemon=True
    t_fixed_table.start()

    c.loop()
