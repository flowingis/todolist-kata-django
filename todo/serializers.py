import uuid

from rest_framework import serializers

from todo.models import Task


class HashTagsField(serializers.Field):
    def to_representation(self, value):
        return value.tags.split(' ')

    def to_internal_value(self, data):
        return {"tags": data}


class TaskSerializer(serializers.ModelSerializer):
    tags = HashTagsField(source='*')

    class Meta:
        model = Task
        fields = ('id', 'uuid', 'description', 'done', 'tags')
        read_only_fields = ('id',)

    def __init__(self, *args, **kwargs):
        if 'context' in kwargs:
            if kwargs['context']['request'].method in ('POST', 'PUT'):
                kwargs['data']['uuid'] = str(uuid.uuid4())
        super(TaskSerializer, self).__init__(*args, **kwargs)
