

import re


def test_contact_details_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)

    email_from_home_page = app.contact.get_contact_list()[0]
    email_from_edit_page = app.contact.get_contact_info_from_edit_page(0)

    adress_from_home_page = app.contact.get_contact_list()[0]
    adress_from_edit_page = app.contact.get_contact_info_from_edit_page(0)

    name_from_home_page = app.contact.get_contact_list()[0]
    name_from_edit_page = app.contact.get_contact_info_from_edit_page(0)

    lastname_from_home_page = app.contact.get_contact_list()[0]
    lastname_from_edit_page = app.contact.get_contact_info_from_edit_page(0)



    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert email_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(email_from_edit_page)

    assert adress_from_home_page.adress == adress_from_edit_page.adress

    assert name_from_home_page.adress == name_from_edit_page.adress

    assert lastname_from_home_page.lastname == lastname_from_edit_page.lastname



def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x !="",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                        [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x !="",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                        [contact.email, contact.email2, contact.email3]))))
