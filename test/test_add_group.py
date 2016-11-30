from model.group import Group

def test_add_group(app):
    app.group.create(Group(name="wada", header="\\65", footer="afsdcas"))
    app.session.logout()



def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))



