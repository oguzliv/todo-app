from django.db import models

# Create your models here.


class User(models.Model):
    user_name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)


class ToDoNote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    created_at = models. DateTimeField('date created')
