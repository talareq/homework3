from model.formfiller import Group

#def test_modify_group(app):
#    app.group.modify_group(Group(name="dupa", header="\\dd", footer="dup"))


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.modify_first_group(Group(name="New Group"))

def test_modify_group_header(app):
   app.group.modify_first_group(Group(header="New Header"))


