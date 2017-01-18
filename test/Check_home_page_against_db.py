from model.formfiller import Contact
import re


def test_check_hp_vs_db(app, db):
    hp_contacts = app.contact.get_contact_list()
    db_contacts = db.get_contact_list()


    hp_firstnames = list(map(lambda a: a.firstname, sorted(hp_contacts, key=Contact.id_or_max)))
    db_firstnames = list(map(lambda b: b.firstname, sorted(db_contacts, key=Contact.id_or_max)))

    assert hp_firstnames == db_firstnames

    hp_lastnames = list(map(lambda c: c.lastname, sorted(hp_contacts, key=Contact.id_or_max)))
    db_lastnames = list(map(lambda d: d.lastname, sorted(hp_contacts, key=Contact.id_or_max)))

    assert hp_lastnames == db_lastnames

    db_phones = list(map(lambda c: merge_phones_like_on_home_page(c), sorted(db_contacts, key=Contact.id_or_max)))
    hp_phones = list(map(lambda f: f.all_phones_from_home_page, sorted(hp_contacts, key=Contact.id_or_max)))

    assert hp_phones == db_phones

    db_merged_emails = merge_emails_like_on_home_page(db_contacts)

    db_emails_like_hp = list(map(lambda c: c.all_emails_from_home_page, sorted(db_merged_emails, key=Contact.id_or_max)))
    hp_emails = list(map(lambda c: c.all_emails_from_home_page, sorted(hp_contacts, key=Contact.id_or_max)))

    assert hp_emails == db_emails_like_hp

    hp_address = list(map(lambda c: c.address, sorted(hp_contacts, key=Contact.id_or_max)))
    db_address = list(map(lambda c: c.address, sorted(hp_contacts, key=Contact.id_or_max)))

    assert hp_address == db_address





def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return list("\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.workphone, contact.mobilephone,
                                        contact.secondaryphone])))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x !="",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                        [contact.email, contact.email2, contact.email3]))))