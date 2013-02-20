# -*- coding: utf-8 -*-

import time
import datetime
import os
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
from termcolor import colored
from todo import TODOManager


class ChangeHandler(FileSystemEventHandler):

    def __init__(self, console_args, *args, **kwargs):
        super(ChangeHandler, self).__init__(*args, **kwargs)
        self.watch = console_args.watchpath
        self.output = console_args.outputpath
        self.is_color = console_args.color
        self.manager = TODOManager(open(self.watch).readlines())
        self.debug = console_args.debug

    def on_modified(self, event):
        if self.watch == os.path.basename(event.src_path):
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


def process(console_args):
    event_handler = ChangeHandler(console_args)
    observer = Observer()
    observer.schedule(event_handler, path=os.getcwd())
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
