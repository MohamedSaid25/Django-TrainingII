from authentication.tests.fixtures import api_client_auth
from rest_framework.test import APIClient
from rest_framework import status
import pytest

# test for login view:


class TestLogin:

    # test if can login successfully
    def test_login_goodData(self, django_user_model, api_client_auth):

        # first create user
        user = django_user_model.objects.create_user(
            username="admin", password="admin")
        client = api_client_auth(user)

        login_data = {'username': "admin", 'password': "admin"}

        response = client.post('/authentication/login/',
                               login_data, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data["token"] is not None

    def test_login_badData(self, django_user_model, api_client_auth):

        user = django_user_model.objects.create_user(
            username="admin", password="admin")
        client = api_client_auth(user)

        login_data = {'username': "adminiiiiiiiiiiin", 'password': "admin"}
        response = client.post('/authentication/login/',
                               login_data, format='json')

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_login_noData(self, django_user_model, api_client_auth):

        user = django_user_model.objects.create_user(
            username="admin", password="admin")
        client = api_client_auth(user)
        login_data = {}
        response = client.post('/authentication/login/',
                               login_data, format='json')
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['username'][0] == "This field may not be blank."
        assert response.data['password'][0] == "This field may not be blank."
