from django.test import TestCase
from users.models import User
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken


def get_client(username, email, password):
    user = User.objects.create_user(username, email, password)
    client = APIClient()
    refresh = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
    return client


class AuthTestCase(TestCase):
    def test_me(self):
        email = "froggagul@gmail.com"
        username = "froggagul"
        password = "1234"

        client = get_client(username, email, password)

        response = client.get("/api/auth/me/", format="json")
        assert response.status_code == 200
        data = response.data
        assert data["email"] == email
        assert data["username"] == username

    def test_me_exception(self):
        client = APIClient()  # no authentications

        response = client.get("/api/auth/me/", format="json")
        assert response.status_code != 200  # get my info must fail
        assert (
            response.data["detail"].code == "not_authenticated"
        )  # error detail includes error detail
