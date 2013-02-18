# -*- coding: utf-8 -*-
import pytest
from sabun.todo import TODOManager


class TestRunning:
    def test_runs(self):
        assert 1 + 1 == 2


class TestTODOManager:

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
        current = ['1', '2', '3']
        manager = TODOManager(current)
        new_data = ['1', '2', '3', '4']
        manager.reload(new_data)
        assert not manager.has_change

    def test_delete_check(self):
        current = ['1', '2', '3']
        manager = TODOManager(current)
        new_data = ['1', '3']
        manager.reload(new_data)
        assert manager.has_change

    def test_get_delete_row(self):
        current = ['1', '2', '3']
        manager = TODOManager(current)
        new_data = ['1', '3']
        manager.reload(new_data)
        assert manager.deleted == ['2']

    def test_not_get_invalid_change(self):
        current = ['1', '   ', '2', '3']
        manager = TODOManager(current)
        new_data = ['1', '2', '3']
        manager.reload(new_data)
        assert not manager.has_change
