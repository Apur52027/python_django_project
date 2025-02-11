from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
   
    path('add_category/',views.add_category,name='add_category'),
    # path('show_data/',views.show_data,name='show_data'),

]