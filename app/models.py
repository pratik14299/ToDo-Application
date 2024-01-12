from django.db import models

# Create your models here.

class TodoTask(models.Model):
    STATUS_CHOICES = [
        ('Y', 'Yes'),
        ('N', 'No'), 
    ] 
    taskName = models.CharField(max_length=200)
    descreption = models.CharField(max_length = 500)
    Status = models.CharField(max_length = 1,choices = STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.taskName},{self.created_at}'

    