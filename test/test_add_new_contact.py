import pytest

from fixture.applicationc import Application
from model.Groupc import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_new_contact(app):
    app.session.login(username="admin",password="secret")
    app.contact.add_new_contact(Group(firstname="g",lastname="wadwa"))
    app.session.logout()

