from model.formfiller import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app


    def add_new_contact(self, contact):
        wd = self.app.wd
        if not len(wd.find_elements_by_name("searchstring")) > 0:
            self.app.open_home_page()
        # add mew contact
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # accept
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contact_cache = None

    def delete_first_contact(self):
        wd = self.app.wd
        self.delete_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        if not len(wd.find_elements_by_name("searchstring")) > 0:
            self.app.open_home_page()
        self.select_contact_by_index(index)
        #submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def modify_first_contact(self):
        wd = self.app.wd
        self.modify_contact_by_index(0)


    def modify_contact_by_index(self, index, contact):
        wd = self.app.wd
        if not len(wd.find_elements_by_name("searchstring")) > 0:
            self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cells = row.find_elements_by_tag_name("td")
        cells[7].click()
        self.fill_contact_form(contact)
        #accept changes
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        self.contact_cache = None



    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))




    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.firstname)
        self.change_field_value("lastname", contact.lastname)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)


    contact_cache = None


    def get_contact_list(self):
        if self.contact_cache is None:

            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(firstname=cells[2].text, id=id))

        return list(self.contact_cache)

