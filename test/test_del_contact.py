from model.formfiller import Contact

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(Contact(firstname="tester", lastname="tester"))
    app.contact.delete_first_contact()
