from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from rest_framework import status
from .models import Task


class TaskAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpass123')
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.task = Task.objects.create(
            title="Initial Task",
            description="Test Description",
            due_date="2025-04-01",
            owner=self.user
        )

    def test_task_list(self):
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_task_create(self):
        data = {
            "title": "New Task",
            "description": "New Description",
            "due_date": "2025-04-05"
        }
        response = self.client.post('/api/tasks/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)

    def test_task_update(self):
        data = {
            "title": "Updated Task",
            "description": "Updated Description",
            "due_date": "2025-04-10",
            "completed": True
        }
        response = self.client.put(f'/api/tasks/{self.task.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, "Updated Task")
        self.assertTrue(self.task.completed)

    def test_task_partial_update(self):
        data = {"completed": True}
        response = self.client.patch(f'/api/tasks/{self.task.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()
        self.assertTrue(self.task.completed)

    def test_task_delete(self):
        response = self.client.delete(f'/api/tasks/{self.task.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)

    def test_unauthenticated_access_denied(self):
        client = APIClient()  # no credentials
        response = client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
