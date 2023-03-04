# First variant

# from django.contrib.auth import get_user_model
# from django.test import TestCase
# from rest_framework import status
# from rest_framework.authtoken.models import Token
# from rest_framework.test import APIClient, APIRequestFactory, APISimpleTestCase, APITestCase, force_authenticate

# User = get_user_model()


# class TestUserViewSet(TestCase):
#     def test_get_user(self):
#         admin = User.objects.create_superuser("admin_1", "admin@admin.com", "admin123456789")
#         client = APIClient()
#         client.login(username="admin_1", password="admin123456789")
#         response = client.get(f"/api/users/{admin.uuid}/")
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

# ----------------------------------------------------------------------------------------------------------------------------------

# Second variant

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, APISimpleTestCase, APITestCase, force_authenticate

from .models import User
from .views import UserModelViewSet


class UserTestCase(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_superuser(username="admin_1", password="12345", email="admintest@mail.ru")
        self.author = User.objects.create(
            first_name="Rechard", last_name="Tolken", birthday_year=1985, email="test@drf.com"
        )

    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get("/api/users/")
        view = UserModelViewSet.as_view({"get": "list"})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_user(self):
        factory = APIRequestFactory()
        request = factory.post(
            "/api/user/",
            {
                "username": "Poet",
                "first_name": "Alexander",
                "last_name": "Pushkin",
                "email": "pushkin@yandex.ru",
                "birthday_year": 1799,
            },
            format="json",
        )
        view = UserModelViewSet.as_view({"post": "create"})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_admin(self):
        factory = APIRequestFactory()
        request = factory.get("/api/users/")
        force_authenticate(request, user=self.user)
        view = UserModelViewSet.as_view({"get": "list"})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_admin_1(self):
        factory = APIRequestFactory()
        request = factory.post("/api/authors/", {"name": "Пушкин", "birthday_year": 1799}, format="json")
        admin = User.objects.create_superuser("admin_2", "admin@admin.com", "admin123456")
        force_authenticate(request, admin)
        view = UserModelViewSet.as_view({"post": "create"})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class UserClientTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_superuser(username="aaaaa@a.com", password="master")
        self.author = User.objects.create(
            first_name="lacaz", last_name="jenderman", birthday_year=2002, email="drfAdmin1@drf.com"
        )

    def test_get_list(self):
        self.client.force_authenticate(self.user)
        response = self.client.get("/api/users/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_list_1(self):
        self.client.force_login(user=self.user)
        response = self.client.get("/api/users/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.client.logout()
        response = self.client.get("/api/users/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # def test_post(self):
    #     self.client.force_login(user=self.user)
    #     response = self.client.post('/api/users/', {
    #         "first_name": "konor",
    #         "last_name": "makcgregar",
    #         "birthday_year": 1992,
    #         "email": "aaaaa@a.com"
    #     })
    #     self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
    #     author = User.objects.get(pk=response.data.get('id'))
    #     self.assertEqual(author.last_name, 'makcgregar')


# Test math function
class TestMath(APISimpleTestCase):
    def test_sqrt(self):
        import math

        self.assertEqual(math.sqrt(4), 2)
