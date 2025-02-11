from django.db import models
from django import forms
from categories.models import Category
# Create your models here.


class TaskModel(models.Model):
    task_title = models.CharField(max_length=200)
    task_description = models.TextField()
    is_completed = models.BooleanField(default=False)
    task_assign_date = models.DateTimeField(auto_now_add=True)
    task =models.ManyToManyField(Category)
    def __str__(self):
        return self.task_title