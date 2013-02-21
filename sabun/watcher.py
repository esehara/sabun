# -*- coding: utf-8 -*-

import time
import datetime
import os
from stat import ST_MTIME
from termcolor import colored
from todo import TODOManager


class ChangeHandler(object):

    def __init__(self, console_args, *args, **kwargs):
        super(ChangeHandler, self).__init__(*args, **kwargs)
        self.watch = console_args.watchpath
        self.output = console_args.outputpath
        self.is_color = console_args.color
        self.manager = TODOManager(open(self.watch).readlines())
        self.debug = console_args.debug
        self.file_time = os.stat(self.watch)[ST_MTIME]

    def reload(self):
        check_time = os.stat(self.watch)[ST_MTIME]
        if self.file_time != check_time:
            self.file_time = check_time
            self._task()

    def _task(self):
        self.manager.reload(
            open(self.watch).readlines(),
            debug=self.debug)

        if self.manager.has_change:
            for line in self.manager.deleted:
                str_date = datetime.datetime.today().strftime(
                    "[%Y-%m-%d %H:%M:%S]")
                line = line.lstrip()

                if self.is_color:
                    str_date_p = colored(
                        str_date, 'cyan')
                    line_p = colored(
                        line.strip(), 'yellow')
                else:
                    str_date_p = str_date
                    line_p = line.strip()

                print str_date_p + "  " + line_p
                log = str_date + "  " + line

                write_file = open(self.output, 'a')
                write_file.write(log)
                write_file.close()
            self.manager.has_change = False


def process(console_args):
    event_handler = ChangeHandler(console_args)

    try:
        while True:
            event_handler.reload()
            time.sleep(1)
    except KeyboardInterrupt:
        os.exit(0)
