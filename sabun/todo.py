# -*- coding: utf-8 -*-


class TODOManager(object):

    def __init__(self, data):

        self.deleted = []
        self.has_change = False
        self.previous = None
        self.current = data

    def _include_check(self, item):

        if len(item) < 1:
            return False

        for check_item in self.current:
            check_item = check_item.lstrip()
            if len(check_item) < 1:
                continue

            if item in check_item:
                self.dp('!! item in check_item !!')
                self.dp('[item]' + item)
                self.dp('[check item]' + check_item)
                return True
            elif check_item in item:
                self.dp('!! check_item in item !!')
                self.dp('[item]' + item)
                self.dp('[check item]' + check_item)
                return True

        return False

    def _comment_out_check(self, item):
        item = item.lstrip()
        for check_item in self.current:
            ls_fix = check_item.lstrip()
            if len(ls_fix) > 0 and check_item.lstrip()[0] == "#":
                return item in ls_fix

    def is_valid(self, item):
        self.dp('Check Item')
        self.dp(item)

        if self._include_check(item):
            self.dp('!! include_check !!')
            return False

        if not item.strip():
            self.dp('!! none line !!')
            return False

        if item.lstrip()[0] == "#":
            self.dp('!! Comment Line !!')
            return False

        if self._comment_out_check(item):
            self.dp('!! Comment Out !!')
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
        self.dp("check_diff > [Row Diff]")
        self.dp(diff)

        diff = self.check_valid(list(diff))
        self.dp("check_diff > [Filtering Diff]")
        self.dp(diff)

        self.has_change = len(diff) > 0

        if self.has_change:
            self.deleted = diff

    def dp(self, message):
        if self.debug:
            print message

    def reload(self, data, debug=None):
        self.debug = debug
        self.previous = self.current
        self.current = data
        self.check_diff()
