from model.group import Group


def test_modify_group_name(app):
    app.group.modify_first_group_two(Group(name="new group"))


def test_modify_group_header(app):
    app.group.modify_first_group_two(Group(header="new header"))