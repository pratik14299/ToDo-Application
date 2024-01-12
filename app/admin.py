from django.contrib import admin
from.models import TodoTask
# Register your models here.

class ToDoAdmin(admin.ModelAdmin):
    model = TodoTask
    list_display = ['id', 'taskName','created_at','updated_at' ]

admin.site.register(TodoTask,  ToDoAdmin) 