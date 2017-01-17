from model.formfiller import Contact
import re


def test_check_hp_vs_db(app, db):
    hp_contacts = app.contact.get_contact_list()
    db_contacts = db.get_contact_list()


#    assert hp_contacts.all_phones_from_home_page == merge_phones_like_on_home_page(db_contacts)



    assert sorted(hp_contacts.firstname, key=Contact.id_or_max) == sorted(db_contacts.firstname, key=Contact.id_or_max)
    assert sorted(hp_contacts.lastname, key=Contact.id_or_max) == sorted(db_contacts.lastname, key=Contact.id_or_max)


    assert sorted(hp_contacts.homephone, key=Contact.id_or_max) == sorted(db_contacts.homephone, key=Contact.id_or_max)
    assert sorted(hp_contacts.workphone, key=Contact.id_or_max) == sorted(db_contacts.workphone, key=Contact.id_or_max)
    assert sorted(hp_contacts.mobilephone, key=Contact.id_or_max) == sorted(db_contacts.mobilephone, key=Contact.id_or_max)
    assert sorted(hp_contacts.secondaryphone, key=Contact.id_or_max) == sorted(db_contacts.secondaryphone, key=Contact.id_or_max)


    assert sorted(hp_contacts.email, key=Contact.id_or_max) == sorted(db_contacts.email, key=Contact.id_or_max)
    assert sorted(hp_contacts.email2, key=Contact.id_or_max) == sorted(db_contacts.email2, key=Contact.id_or_max)
    assert sorted(hp_contacts.adress, key=Contact.id_or_max) == sorted(db_contacts.adress, key=Contact.id_or_max)



def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return list("\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.workphone, contact.mobilephone,
                                        contact.secondaryphone])))))