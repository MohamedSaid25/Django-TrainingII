from authentication.tests.fixtures import api_client_auth
from rest_framework import status


class TestUserView:
    username = "Narutooooooo"
    password = "rasingan20x404"

    """
     
    """

    # auth can get good data => test_if_auth_GetGoodData
    def test_if_auth_GetGoodData(self, django_user_model, api_client_auth):
        user = django_user_model.objects.create_user(
            username=self.username, password=self.password)
        client = api_client_auth(user)
        response = client.get("/users/1/")
        assert response.status_code == status.HTTP_200_OK
        assert response.data["username"] == self.username
        assert response.data["id"] == 1
    # Un_auth can get good data => test_if_auth_GetGoodData

    def test_Unuth_GetGoodData(self, django_user_model, api_client_auth):
        user = django_user_model.objects.create_user(
            username=self.username, password=self.password)
        client = api_client_auth()
        response = client.get("/users/1/")
        assert response.status_code == status.HTTP_200_OK
        assert response.data["username"] == self.username
        assert response.data["id"] == 1
    # Not exist user Un _uth

    def test_AcessNotExist(self, api_client_auth):
        client = api_client_auth()
        response = client.get("/users/1/")
        assert response.status_code == status.HTTP_404_NOT_FOUND
