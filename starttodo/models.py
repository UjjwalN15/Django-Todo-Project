from django.db import models

# Create your models here.

class Todo_Table(models.Model):
    Status_Choices = [
        ('In progress', 'In progress'),
        ('Not started', 'Not started'),
        ('Completed', 'Completed'),
    ]
    Name = models.CharField(max_length=200)
    Description = models.TextField()
    Status = models.CharField(max_length=200, choices = Status_Choices)
    def __str__(self):
        return f"{self.Name} - {self.Status}"