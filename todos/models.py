from django.db import models

# Create your models here.

class ToDoList(models.Model):
    name = models.CharField(max_length=100)
    created_on = models.DateTimeField(null=True)

