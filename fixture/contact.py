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
