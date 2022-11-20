from authentication.tests.fixtures import api_client_auth
from rest_framework import status


class Test:

    def test_if_authCanGet(self, django_user_model, api_client_auth):
        user = django_user_model.objects.create_user(
            username="task7", password="task7")
        client = api_client_auth(user)
        response = client.get('/artists/')

        assert response.status_code == status.HTTP_200_OK

    def test_if_UnauthCanGet(self, api_client_auth):
        client = api_client_auth()
        response = client.get('/artists/')
        assert response.status_code == status.HTTP_200_OK

    def test_if_unauthenticated_canNot_post(self, api_client_auth):
        client = api_client_auth()
        artist = {'stageName': 'deadman',
                  'socialMediaProfile': 'sadboy@haha.com'}
        response = client.post('/artists/', artist, format='json')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    #

    def test_if_auth_can_post_withEmptyData(self, django_user_model, api_client_auth):
        user = django_user_model.objects.create_user(
            username="task7", password="task7")
        client = api_client_auth(user)
        artist = {'stageName': '',
                  'socialMediaProfile': 'Aoooo@haha.com'}

        response = client.post('/artists/', artist, format='json')
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['stageName'][0] == "This field may not be blank."

    def test_if_auth_can_post_with_correctData(self, django_user_model, api_client_auth):
        user = django_user_model.objects.create_user(
            username="task7", password="task7")
        client = api_client_auth(user)
        artist = {'stageName': 'moksh2AA5_',
                  'socialMediaProfile': 'Aoooo@haha.com'}

        response = client.post('/artists/', artist, format='json')
        assert response.status_code == status.HTTP_201_CREATED
