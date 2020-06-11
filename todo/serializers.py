import uuid

from rest_framework import serializers

from todo.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'uuid', 'description', 'done')
        read_only_fields = ('id',)

    def __init__(self, *args, **kwargs):
        if 'context' in kwargs:
            if kwargs['context']['request'].method in ('POST', 'PUT'):
                kwargs['data']['uuid'] = str(uuid.uuid4())
        super(TaskSerializer, self).__init__(*args, **kwargs)
