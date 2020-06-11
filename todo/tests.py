import uuid

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase

from todo.models import Task
from todo.serializers import TaskSerializer


class TaskTestCase(TestCase):
    def setUp(self):
        Task.objects.create(
            uuid=str(uuid.uuid4()),
            description="Primo Task"
        )
        Task.objects.create(
            uuid=str(uuid.uuid4()),
            description="Secondo Task"
        )

    def test_task_list_count(self):
        tasks = Task.objects.all()
        self.assertEqual(2, len(tasks))

    def test_first_task_description(self):
        first_task = Task.objects.get(id=1)
        self.assertIsNotNone(first_task)
        self.assertEqual("Primo Task", first_task.description)

    def test_serializer(self):
        first_task = Task.objects.get(id=1)
        serializer = TaskSerializer(instance=first_task)
        data = serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'uuid', 'description', 'done']))


class TaskAPITestCase(APITestCase):
    def setUp(self):
        Task.objects.create(
            uuid=str(uuid.uuid4()),
            description="Primo Task"
        )
        Task.objects.create(
            uuid=str(uuid.uuid4()),
            description="Secondo Task"
        )
        Task.objects.create(
            uuid=str(uuid.uuid4()),
            description="Task Fatto",
            done=1
        )

    def test_list(self):
        response = self.client.get('/api/tasks/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(3, Task.objects.count())

    def test_get(self):
        response = self.client.get('/api/tasks/1/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.data;
        self.assertEqual('Primo Task', data['description'])

    def test_insert(self):
        data = r'{"description": "New Task from API client"}'
        response = self.client.post('/api/tasks/', data=data, content_type="application/json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update(self):
        data = r'{"description": "New Task from API client ***MODIFICATO***"}'
        response = self.client.put('/api/tasks/1/', data=data, content_type="application/json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete(self):
        response = self.client.delete('/api/tasks/1/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_done(self):
        new_task = Task.objects.create(
            uuid=str(uuid.uuid4()),
            description="Nuovo Task"
        )
        done_before_update = new_task.done
        response = self.client.post('/api/tasks/4/done/')

        new_task.refresh_from_db()
        done_after_update = new_task.done

        self.assertEqual(0, done_before_update)
        self.assertEqual(1, done_after_update)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_undone(self):
        task = Task.objects.get(id=3)
        done_before_update = task.done
        response = self.client.post('/api/tasks/3/undone/')

        task.refresh_from_db()
        done_after_update = task.done

        self.assertEqual(1, done_before_update)
        self.assertEqual(0, done_after_update)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

