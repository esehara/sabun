# -*- coding: utf-8 -*-


class TODOManager(object):

    def __init__(self, data):

        self.deleted = []
        self.has_change = False
        self.previous = None
        self.current = data

    def _include_check(self, item):

        for check_item in self.current:
            if item in check_item:
                return True
            elif check_item in item:
                return True
        return False

    def _comment_out_check(self, item):
        for check_item in self.current:
            ls_fix = check_item.lstrip()
            if len(ls_fix) > 0 and check_item.lstrip()[0] == "#":
                return check_item.lstrip()[0] in check_item

    def is_valid(self, item):

        if self._include_check(item):
            return False

        if not item.strip():
            return False

        if item.lstrip()[0] == "#":
            return False

        if self._comment_out_check(item):
            return False

        return True

    def check_valid(self, diff):
        valid_diff = []

        for item in diff:
            if self.is_valid(item):
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
