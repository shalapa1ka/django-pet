from django.urls import path, include
from .views import (
    TodoListApiView,
    TodoDetailApiView
)

urlpatterns = [
    path('api/', TodoListApiView.as_view(), name='todo-list-api'),
    path('api/<int:todo_id>', TodoDetailApiView.as_view(), name='todo-detail-api')
]
