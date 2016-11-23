from model.group import Contact

def test_add_new_contact(app):

    app.session.login(username="admin",password="secret")
    app.contact.add_new_contact(Contact(firstname="g",lastname="wadwa"))
    app.session.logout()

