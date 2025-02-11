from django.shortcuts import render,redirect
from taskmodel.forms import TaskModel
def home(request):
  form =TaskModel.objects.all()
  return render(request,'home.html',{'form' :form})