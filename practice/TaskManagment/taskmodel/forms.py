
from django import forms
from .models import TaskModel
from categories.models import Category
class TaskForm(forms.ModelForm):
    class Meta:
        
        model = TaskModel
        fields ='__all__'