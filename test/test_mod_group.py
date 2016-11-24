from model.group import Group

def test_modify_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_group(Group(name="dupa", header="\\dd", footer="dup"))
    app.session.logout()

