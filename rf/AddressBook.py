
import json
import os.path
from fixture.application import Application
from fixture.db import Dbfixture
from model.formfiller import Group

class AddressBook:

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self, config="target.json", browser="chrome"):
        self.browser = browser
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),"..", config)
        with open(config_file) as f:
            self.target = json.load(f)

    def init_fixtures(self):
        web_config = self.target["web"]
        self.fixtures = Application(browser=self.browser, base_url=web_config["baseUrl"])
        db_config = self.target["db"]
        self.dbfixture = Dbfixture(host=db_config["host"], name=db_config["name"], user=db_config["user"],
                              password=db_config["password"])

    def destroy_fixtures(self):
        self.dbfixture.destroy()
        self.fixtures.destroy()


    def create_group(self, name, header, footer):
        self.fixtures.group.create(Group(name=name, header=header, footer= footer))