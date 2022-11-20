from authentication.tests.fixtures import api_client_auth
from rest_framework.test import APIClient
from rest_framework import status
import pytest

# test for register view:


class TestRegister:
    username = "mokshaaaaa"
    email = "fcis@gmail"
    password = "lollololololololxd_sadBoy"
    bio = 'task7 testing'

    # test with good data
    def test_register(self, api_client_auth):
        client = api_client_auth()
        obj = {'username': self.username, 'email': self.email,
               'password1': self.password, 'password2': self.password}

        response = client.post('/authentication/register/', obj, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["username"] == self.username
        assert response.data["email"] == self.email

    def test_register_BadData(self, api_client_auth):
        client = api_client_auth()

        self.password = "WWEWEQQWQW7879"

        obj = {'username': self.username, 'email': self.email,
               'password1': self.password, 'password2': self.password}

        response = client.post('/authentication/register/', obj, format='json')
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data["password1"][0].code == "this username already exist try another one"
        assert response.data["password1"][0].code == "two passwords must be same"
        assert response.data["password1"][0].code == "Can not be empty"
        assert response.data["password1"][0].code == "Password too short"
