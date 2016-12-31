from model.formfiller import Contact
import random

def test_delete_random_contact(app, db):
    if app.contact.count() == 0:
        app.contact.add_new_contact(Contact(firstname="tester", lastname="tester"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
