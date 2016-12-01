class ContactHelper:

    def __init__(self, app):
        self.app = app


    def add_new_contact(self, contact):
        wd = self.app.wd
        # add mew contact
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # accept
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()


    def delete_first_contact(self):
        wd = self.app.wd
        #select first contact
        wd.find_element_by_name("selected[]").click()
        #submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()

    def modify_first_contact(self, contact):
        wd = self.app.wd
        #click edit button on first contact
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        #edit name and lastname
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        # enter first name
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        # enter surname
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        #accept changes
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        wd.find_element_by_name("searchstring").click()
        wd.find_element_by_name("searchstring").send_keys("\\9")

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))


    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)