from fixture.orm import ORMfixture
from model.formfiller import Group


db = ORMfixture(host="127.0.0.1", name="addressbook", user="root", password="")


try:
    l = db.get_contacts_in_group(Group(id="12"))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass #db.destroy()