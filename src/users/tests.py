from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class ViewTest(TestCase):
    def setUp(self):
        User.objects.create_user(username="dummy", password="1234567!")

    def test_user_auth_login(self):
        response = self.client.get(reverse('users:login'))
        self.assertEqual(response.status_code, 200)

    def test_user_auth_register(self):
        response = self.client.get(reverse('users:register'))
        self.assertEqual(response.status_code, 200)

    def test_user_auth_user(self):
        self.client.login(username="dummy", password="1234567!")
        response = self.client.get(reverse('users:user'))
        self.assertEqual(response.status_code, 200)

    def test_user_no_auth_user(self):
        response = self.client.get(reverse('users:user'))
        self.assertEqual(response.status_code, 302)

    def test_user_auth_users_all(self):
        self.client.login(username="dummy", password="1234567!")
        response = self.client.get(reverse('users:users-all'))
        self.assertEqual(response.status_code, 200)

    def test_user_no_auth_users_all(self):
        response = self.client.get(reverse('users:users-all'))
        self.assertEqual(response.status_code, 302)

    def test_user_no_auth_other_user(self):
        response = self.client.get(reverse('users:other-user'))
        self.assertEqual(response.status_code, 302)

    def test_user_no_auth_detail(self):
        response = self.client.get(reverse('users:user-detail'))
        self.assertEqual(response.status_code, 302)


