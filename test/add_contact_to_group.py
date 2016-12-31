from model.formfiller import Contact
from fixture.orm import ORMfixture
from model.formfiller import Group


db = ORMfixture(host="127.0.0.1", name="addressbook", user="root", password="")



def test_add_contact_to_group(app, json_contacts):
    contact = json_contacts
    old_contacts = db.get_contacts_in_group(Group(id="12"))
    app.contact.add_contact_to_group(contact)
    new_contacts = db.get_contacts_in_group(Group(id="12"))
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)