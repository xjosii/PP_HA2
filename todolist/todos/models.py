from django.db import models


class ListEntry(models.Model):
    task = models.CharField(max_length=160)
    deadline = models.CharField(max_length=10)
    progress = models.CharField(max_length=5)