from django.http import Http404, HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action

from todo.fake_permission import FakePermission
from todo.models import Task
from todo.serializers import TaskSerializer


def index(request):
    return render(request, 'todo/index.html', {})


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-id')
    serializer_class = TaskSerializer
    permission_classes = (FakePermission,)

    @action(detail=True, methods=['post'])
    def done(self, request, pk):
        try:
            task = Task.objects.get(id=pk)
        except Task.DoesNotExist:
            raise Http404
        task.done = 1
        task.save()
        return HttpResponse(status=204)
