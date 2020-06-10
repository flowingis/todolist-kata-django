import uuid

from rest_framework import serializers

from todo.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'uuid', 'description')
        read_only_fields = ('id',)

    def __init__(self, *args, **kwargs):
        if kwargs['context']['request'].method == 'POST':
            kwargs['data']['uuid'] = str(uuid.uuid4())
        super(TaskSerializer, self).__init__(*args, **kwargs)
