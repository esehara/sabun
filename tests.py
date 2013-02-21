# -*- coding: utf-8 -*-
import pytest
from sabun.todo import TODOManager


class TestRunning:
    def test_runs(self):
        assert 1 + 1 == 2


class TestTODOManager:

    def _datadriven_assert(self, current, new_data, should):
        manager = TODOManager(current)
        manager.reload(new_data)
        if should == "not change":
            assert not manager.has_change
        elif should == "has change":
            assert manager.has_change
        else:
            assert not "has argument error "

    def has_change(self, current, new_data):
        self._datadriven_assert(current, new_data, 'has change')

    def not_change(self, current, new_data):
        self._datadriven_assert(current, new_data, 'not change')

    def test_current_to_previous(self):

        current = ('1', '2', '3')
        manager = TODOManager(current)
        assert manager.previous != manager.current

        new_data = ('4', '5', '6')
        manager.reload(new_data)
        assert manager.previous == current

    def test_check_modify(self):
        current = ['1', '2', '3']
        manager = TODOManager(current)
        manager.reload(current)
        assert manager.previous == manager.current
        assert not manager.has_change

        new_data = ['1', '3']
        manager.reload(new_data)
        assert manager.has_change

    def test_add_is_not_check(self):
        self.not_change(
            ['1', '2', '3'],
            ['1', '2', '3', '4'])

    def test_delete_check(self):
        self.has_change(
            ['1', '2', '3'],
            ['1', '3'])

    def test_get_delete_row(self):
        current = ['1', '2', '3']
        manager = TODOManager(current)
        new_data = ['1', '3']
        manager.reload(new_data)
        assert manager.deleted == ['2']

    def test_not_get_invalid_change(self):
        self.not_change(
            ['1', '   ', '2', '3'],
            ['1', '2', '3'])

        self.has_change(
            ['1', '  ', '2', '3'],
            ['1', '  ', '3'])

    def test_whitespace_bug_fix(self):
        self.has_change(
            ['1', '', '2', '3'],
            ['1', '', '3'])

        self.has_change(
            ['1', '', '2', ''],
            ['1', ''])

    def test_prefix_not_logging(self):
        self.not_change(
            ['1', '#2', '3'],
            ['1', '3'])

    def test_if_include_not_fix(self):
        self.not_change(
            ['1', '2', '3'],
            ['1', 'A 2', '3'])

        self.not_change(
            ['1', 'A 2', '3'],
            ['1', '2', '3'])

    def test_comment_out_is_not_pick(self):
        self.not_change(
            ['1', '2', '3'],
            ['1', '# 2', '   #3'])

        self.has_change(
            ['1', '2', '3'],
            ['1', '# 2'])

        self.not_change(
            ['1', '  2', '3'],
            ['1', ' #2', '3'])
