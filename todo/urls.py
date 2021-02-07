from django.urls import path, include
from .views import *

app_name = 'todo'

urlpatterns = [
    path('', index, name='todo_list'),
    path('update/<str:pk>', update, name='todo_update'),
    path('delete/<str:pk>', delete, name='todo_delete'),
]