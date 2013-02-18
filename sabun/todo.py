# -*- coding: utf-8 -*-


class TODOManager(object):

    def __init__(self, data):

        self.deleted = []
        self.has_change = False
        self.previous = None
        self.current = data

    def check_valid(self, diff):
        valid_diff = []

        for item in diff:
            if item.strip():
                valid_diff.append(item)

        return valid_diff

    def check_diff(self):
        diff = set(self.previous) - set(self.current)
        diff = self.check_valid(list(diff))
        self.has_change = len(diff) > 0

        if self.has_change:
            self.deleted = diff

    def reload(self, data):

        self.previous = self.current
        self.current = data
        self.check_diff()
