from django import forms
from .models import TodoTask


class ToDoForm(forms.ModelForm):
    
    class Meta:
        model = TodoTask
        fields = "__all__"
        labels = {
            "taskName":"Task",
            "descreption":"Description",

        }
 