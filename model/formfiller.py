from sys import maxsize

class Group:

    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.name)


    def __eq__(self, other):
        #return self.id == other.id and self.name == other.name
        return (self.id is None or other.id is None or self.id== other.id) and self.name == other.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize



class Contact:

    def __init__(self, firstname=None, lastname=None, homephone=None,
                 mobilephone=None, workphone=None, secondaryphone=None,
                 id=None, all_phones_from_home_page=None, all_emails_from_home_page=None,
                 email=None, email2=None, email3=None, adress=None):
        self.firstname=firstname
        self.lastname=lastname
        self.homephone=homephone
        self.mobilephone=mobilephone
        self.workphone=workphone
        self.secondaryphone=secondaryphone
        self.id = id
        self.all_phones_from_home_page=all_phones_from_home_page
        self.all_emails_from_home_page=all_emails_from_home_page
        self.email=email
        self.email2=email2
        self.email3=email3
        self.adress=adress

    def __repr__(self):
        return "%s:%s" % (self.id, self.firstname)


    def __eq__(self, other):
        #return self.id == other.id and self.name == other.name
        return (self.id is None or other.id is None or self.id== other.id) and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize






