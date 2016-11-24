class ContactHelper:

    def __init__(self, app):
        self.app = app


    def add_new_contact(self, group):
        wd = self.app.wd
        # add mew contact
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        # enter first name
        wd.find_element_by_name("firstname").send_keys(group.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        # enter surname
        wd.find_element_by_name("lastname").send_keys(group.lastname)
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