from datetime import datetime
from rest_framework.test import APIClient
from django.urls import reverse
import pytest
from accounts.models import User


@pytest.fixture
def my_user():
    user = User.objects.create_user(
        email="user2@example.com", password="password12345", is_verified=True
    )
    return user


@pytest.mark.django_db
class TestPostApi:
    client = APIClient()

    # def test_get_post_response_200_status(self):

    #     url = reverse("blog:api-v1:post-list")

    #     response = self.client.get(url)
    #     assert response.status_code == 200

    def test_create_post_response_401_status(self, my_user):

        url = reverse("blog:api-v1:post-list")
        data = {
            "title": "pytest",
            "content": "test content",
            "status": True,
            "published_data": datetime.now(),
        }
        response = self.client.post(url, data)
        assert response.status_code == 401

    # def test_create_post_response_201_status(self, my_user):

    #     url = reverse("blog:api-v1:post-list")
    #     data = {
    #         "title": "pytest",
    #         "content": "test content",
    #         "status": True,
    #         "published_data": datetime.now(),
    #     }
    #     self.client.force_authenticate(user=my_user)
    #     response = self.client.post(url, data)
    #     assert response.status_code == 201

    def test_create_post_invali_response_400_status(self, my_user):

        url = reverse("blog:api-v1:post-list")
        data = {
            "title": "pytest",
            "content": "test content",
        }
        self.client.force_authenticate(user=my_user)
        response = self.client.post(url, data)
        assert response.status_code == 400
