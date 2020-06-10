from django.shortcuts import render
from rest_framework import viewsets

from todo.fake_permission import FakePermission
from todo.models import Task
from todo.serializers import TaskSerializer


def index(request):
    return render(request, 'todo/index.html', {})


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (FakePermission,)


