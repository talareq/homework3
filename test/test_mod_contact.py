from model.formfiller import Contact


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(Contact(firstname="tester", lastname="tester"))
    app.contact.modify_first_contact(Contact(firstname="roman", lastname="erotoman"))

