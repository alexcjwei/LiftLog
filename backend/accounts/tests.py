from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from accounts import models


class SignupViewTests(TestCase):
    def test_signup_no_duplicate_email(self):
        # Create a user with the same email as the one we're going to try to sign up with
        User.objects.create_user(
            username="testuser", email="test@test.com", password="testpassword"
        )
        response = self.client.post(
            reverse("accounts:signup"),
            {
                "username": "testuser2",
                "email": "test@test.com",
                "password": "testpassword",
            },
        )
        self.assertContains(response, "A user with that email already exists.")
        self.assertFalse(User.objects.filter(username="testuser2").exists())
        self.assertFalse(
            models.Profile.objects.filter(user__username="testuser2").exists()
        )
