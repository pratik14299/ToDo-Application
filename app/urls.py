from django.urls import path
from . import views

urlpatterns = [
    path('create/',views.AddTask,name = 'create_url'),
    path('show/',views.ShowTask,name = 'show_url'),
    path('update/<int:id>',views.updateTask,name = 'update_url'),
    path('delete/<int:id>',views.DeleteTask,name = "delete_url")
]

