from django.urls import path
from . import views

urlpatterns = [
    path('', views.dailyTask, name="task" ), 
    path('create-task/', views.CreateTask, name="create-task" ), 
    path('task-popup/', views.taskModalPopup, name="task-popup"),
    path('update-task/', views.UpdateTask, name="update-task"),
    path('delete-task/', views.deleteTask, name="delete-task"),
    path('task-data-autoload/', views.TaskDataAutoloader, name="task-data-autoload"),  
    # path('view-task/<str:pk>', views.viewTask, name="view-task" ),
    # path('update-task/<str:pk>', views.updateTask, name="update-task" ),
    # path('delete-task/<str:pk>', views.deleteTask, name="delete-task" ), 
]
