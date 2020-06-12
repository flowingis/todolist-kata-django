from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.core import serializers
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

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

    @action(detail=False, methods=['get'])
    def search(self, request):
        query_data = {
            'description': request.query_params['description'],
            'tags': request.query_params['tags']
        }
        raw_data = Task.objects.raw(
            self.__get_sql_for_search(query_data),
            self.__get_sql_params_for_search(query_data)
        )
        #TODO: EMPTY RAW DATA
        data = serializers.serialize("json", raw_data)
        return Response(data)

    def __update_done_status(self, request, pk, done):
        try:
            task = Task.objects.get(id=pk)
        except Task.DoesNotExist:
            raise Http404
        task.done = done
        task.save()
        return HttpResponse(status=204)

    def __get_sql_params_for_search(self, query_data: dict):
        sql_params = []
        if query_data['description']:
            sql_params.append('%' + query_data['description'] + '%')
        if query_data['tags']:
            sql_params.append(','.join(
                list(
                    map(lambda tag: "'" + tag + "'", query_data['tags'].split(' ')))
                )
            )

        return sql_params

    def __get_sql_for_search(self, query_data: dict):
        sql: str = '''
            WITH RECURSIVE split(id, uuid, description, done, tags, tag_name, rest) AS (
              SELECT id, uuid, description, done, tags, '', tags || ' ' FROM main.todo_task WHERE id
               UNION ALL
              SELECT id,
                     uuid,
                     description,
                     done,
                     tags,
                     substr(rest, 0, instr(rest, ' ')),
                     substr(rest, instr(rest, ' ')+1)
                FROM split
               WHERE rest <> '')
            SELECT DISTINCT id, uuid, description, done, tags
              FROM split             
              WHERE 1=1
        '''
        if query_data['description']:
            sql += ' AND description LIKE %s'
        if query_data['tags']:
            sql += ' AND tag_name IN (%s)'
        sql += ' ORDER BY id desc'
        return sql
