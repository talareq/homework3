from model.formfiller import Contact
import random


def test_modify_first_contact(app, db):

    if app.contact.count() == 0:
        app.contact.add_new_contact(Contact(firstname="tester", lastname="tester"))
    old_contacts = db.get_contact_list()
    old_contact = random.choice(old_contacts)
    contact = Contact(firstname="roman", lastname="erotoman")
    contact.id = old_contact.id
    app.contact.modify_contact_by_id(old_contact.id, contact)
    new_contacts = db.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

