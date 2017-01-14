from model.formfiller import Contact
from fixture.orm import ORMfixture
from model.formfiller import Group
import random

db = ORMfixture(host="127.0.0.1", name="addressbook", user="root", password="")



def test_add_contact_to_group(app):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.contact.add_contact_to_group(contact.id, group)
    new_contacts = db.get_contact_list()
    old_contacts.append()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

