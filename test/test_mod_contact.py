from model.formfiller import Contact


def test_modify_first_contact(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.add_new_contact(Contact(firstname="tester", lastname="tester"))
    contact = Contact(firstname="roman", lastname="erotoman")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

