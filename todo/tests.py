import uuid

from django.test import TestCase

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
        self.assertEqual(set(data.keys()), set(['id', 'uuid', 'description']))
