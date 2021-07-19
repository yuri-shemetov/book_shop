from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class ViewTest(TestCase):
    def setUp(self):
        User.objects.create_user(username="dummy", password="1234567!")

    def test_user_main(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_user_page_books(self):
        response = self.client.get(reverse('books'))
        self.assertEqual(response.status_code, 200)

    def test_user_page_promo(self):
        response = self.client.get(reverse('promo'))
        self.assertEqual(response.status_code, 302)

    def test_user_no_auth_user_rating(self):
        response = self.client.get(reverse('raiting'))
        self.assertEqual(response.status_code, 302)

    def test_user_auth_user_rating(self):
        self.client.login(username="dummy", password="1234567!")
        response = self.client.get(reverse('raiting'))
        self.assertEqual(response.status_code, 200)

    def test_user_no_auth_administration(self):
        response = self.client.get(reverse('administration'))
        self.assertEqual(response.status_code, 302)
