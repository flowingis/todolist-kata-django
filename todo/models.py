from django.db import models


class Task(models.Model):
    uuid = models.CharField(max_length=36)
    description = models.CharField(max_length=255)
    done = models.SmallIntegerField(default=0)
    tags = models.CharField(max_length=255, default='')
