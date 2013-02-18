# -*- coding: utf-8 -*-

import time
import datetime
import os
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
from todo import TODOManager


class ChangeHandler(FileSystemEventHandler):

    def __init__(self, filepath, outputpath, *args, **kwargs):
        super(ChangeHandler, self).__init__(*args, **kwargs)
        self.watch = filepath
        self.output = outputpath
        self.manager = TODOManager(open(filepath).readlines())

    def on_modified(self, event):
        if self.watch == os.path.basename(event.src_path):
            self.manager.reload(open(self.watch).readlines())

            if self.manager.has_change:
                for line in self.manager.deleted:
                    str_date = datetime.datetime.today().strftime(
                        "%Y-%m-%d %H:%M:%S")
                    log = str_date + "  " + line.lstrip()
                    print log.strip()

                    write_file = open(self.output, 'a')
                    write_file.write(log)
                    write_file.close()


def process(filepath, output):
    event_handler = ChangeHandler(filepath, output)
    observer = Observer()
    observer.schedule(event_handler, path=os.getcwd())
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
