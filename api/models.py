from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=255)
    group = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    priority = models.IntegerField()
    quantity = models.IntegerField()
    deadline = models.CharField(max_length=255)
    additional_info = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name