# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinilizer(fixture.destroy)
    return fixture

def test_add_group(app):

    app.login(wd, username="admin", password="secret")
    app.open_groups_page(wd)
    app.group_creation(wd, Group(name="wada", header="\\65", footer="afsdcas"))
    app.logout(wd)


def test_add_empty_group(app):

    app.login( username="admin", password="secret")
    app.group_creation( Group(name="", header="", footer=""))
    app.logout()


