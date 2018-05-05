# -*- coding: utf-8 -*-
from model.group import Group


def test_homeworkone(app):
        old_groups = app.group.get_group_list()
        app.group.create(Group(name="group name", header="header name", footer="footer name"))
        new_groups = app.group.get_group_list()
        assert len(old_groups) + 1 == len(new_groups)

def test_empty_group_homeworkone(app):
        old_groups = app.group.get_group_list()
        app.group.create(Group(name="", header="", footer=""))
        new_groups = app.group.get_group_list()
        assert len(old_groups) + 1 == len(new_groups)
