from model.formfiller import Contact
from fixture.orm import ORMfixture
from model.formfiller import Group
import random

db = ORMfixture(host="127.0.0.1", name="addressbook", user="root", password="")



def test_add_contact_to_group(app, json_contacts):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    contact = json_contacts
    old_contacts = db.get_contacts_in_group(group)
    app.contact.add_contact_to_group(contact, group.id)
    new_contacts = db.get_contacts_in_group(group)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

