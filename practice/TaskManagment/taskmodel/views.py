from django.shortcuts import render,redirect
from .forms import TaskForm
from .models import TaskModel
from .import forms,models
# Create your views here.
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_task')
    else:
        form = TaskForm()
    return render(request, 'add_task.html',{'form':form})

def edit_task(request, id):
    task= models.TaskModel.objects.get(pk=id)
    form =forms.TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    return render(request,'add_task.html',{'form' :form})
def delete_task(request, id):
    task = models.TaskModel.objects.get(pk=id) 
    task.delete()
    return redirect('homepage')