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
        return self.__update_done_status(self, pk, 1)

    @action(detail=True, methods=['post'])
    def undone(self, request, pk):
        return self.__update_done_status(self, pk, 0)

    def __update_done_status(self, request, pk, done):
        try:
            task = Task.objects.get(id=pk)
        except Task.DoesNotExist:
            raise Http404
        task.done = done
        task.save()
        return HttpResponse(status=204)
