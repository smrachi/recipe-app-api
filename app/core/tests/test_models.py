from django.tests import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        '''test creating a new user with email is successful'''
        email = 'mohsen@smr.com'
        password = 'SMR138823smr'
        user = get_user_model.objects.create_user(
            email = email,
            password = password
        )
