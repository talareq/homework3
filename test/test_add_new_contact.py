from model.formfiller import Contact

def test_add_new_contact(app):

    app.contact.add_new_contact(Contact(firstname="g",lastname="wadwa"))


