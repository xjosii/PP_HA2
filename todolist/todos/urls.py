from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.todos_table,name='todo_table'), #/todos/ siehe urls.py in todolist
    path('entry/',views.todos_add, name='add_listEntry'), #/todos/entry/
    path('entry/<int:id>/',views.todos_edit,name='edit_listEntry'),
    path('delete/<int:id>/', views.todos_delete, name='delete_listEntry'),
]
