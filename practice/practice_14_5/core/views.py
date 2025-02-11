from django.shortcuts import render
from .forms import ExampleForm
# Create your views here.

def home(request):
  form =ExampleForm()
  return render(request,'home.html',{'form':form })