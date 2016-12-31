from model.formfiller import Contact
from fixture.orm import ORMfixture
from model.formfiller import Group
from model.formfiller import Contact
import random



db = ORMfixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_delete_random_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(Contact(firstname="tester", lastname="tester"))
    old_contacts = db.get_contacts_in_group(Group(id="12"))
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contacts_in_group(Group(id="12"))
    old_contacts.remove(contact)
    assert old_contacts == new_contacts