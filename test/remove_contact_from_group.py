from model.formfiller import Contact
from fixture.orm import ORMfixture
from model.formfiller import Group
from model.formfiller import Contact
import random



db = ORMfixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_delete_random_contact(app):

    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    if len(db.get_contacts_in_group(group)) == 0:
        app.contact.add_contact_to_group(Contact(firstname="tester", lastname="tester"), group)
    old_contacts = db.get_contacts_in_group(group)
    removed_contacts = db.get_contacts_not_in_group(group)
    def rem_con(old_contacts):
        if old_contacts in removed_contacts:
            return True
        else:
            return False
    filter(rem_con, old_contacts )
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = old_contacts.remove(contact)
    assert old_contacts == new_contacts