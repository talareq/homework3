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

    def __init__(self, firstname=None, middlename=None, lastname=None, id=None):
        self.firstname=firstname
        self.middlename=middlename
        self.lastname=lastname
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.firstname)


    def __eq__(self, other):
        #return self.id == other.id and self.name == other.name
        return (self.id is None or other.id is None or self.id== other.id) and self.firstname == other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize






