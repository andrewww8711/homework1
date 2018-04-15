# -*- coding: utf-8 -*-
from contact import Group
from Application_home_work import Application_home
import pytest


@pytest.fixture
def app(request):
    fixture = Application_home()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_address_book(app):
        app.login(username="admin", password="secret")
        app.create_address_book(Group(firstname="Ivan", lastname="Ivanov", title="QA Engineer", company="Google", address="123 main street", homephone="123456", cellphone="1234567",
                                 email="test@mail.com"))
        app.logout()


def test_empty_add_address_book(app):
        app.login(username="admin", password="secret")
        app.create_address_book(Group(firstname="", lastname="", title="", company="", address="", homephone="", cellphone="",
                                 email=""))
        app.logout()