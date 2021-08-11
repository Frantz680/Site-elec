from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class UserLogin(TestCase):

    def setUp(self):
        User.objects.create(username='test', password="123test")

    def test_login(self):
        response = self.client.post(reverse('login'),
                                    {'username': 'test1',
                                     'password': '123test'}, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_register(self):
        response = self.client.post(reverse('register'),
                                    {'username': 'test',
                                     'email': 'test@hotmail.fr',
                                     'password1': '123456test',
                                     'password2': '123456test'}, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        self.client.login(username='test', password='123test')
        self.client.logout()
        self.assertRaises(
            KeyError, lambda: self.client.session['_auth_user_id'])


class PageTestCase(TestCase):

    def test_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_add_picture_carrousel_page(self):
        response = self.client.get(reverse('add_picture_carrousel'))
        self.assertEqual(response.status_code, 200)

    def test_add_actu_page(self):
        response = self.client.get(reverse('add_actu'))
        self.assertEqual(response.status_code, 200)

    def test_add_cat_page(self):
        response = self.client.get(reverse('add_cat'))
        self.assertEqual(response.status_code, 200)

    def test_all_actu_page(self):
        response = self.client.get(reverse('all_actu'))
        self.assertEqual(response.status_code, 200)

    def test_logout_page(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)

    def test_register_page(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

    def test_mentions_legales_page(self):
        response = self.client.get(reverse('ml'))
        self.assertEqual(response.status_code, 200)

    def test_my_account_page(self):
        response = self.client.get(reverse('my_account'))
        self.assertEqual(response.status_code, 302)
