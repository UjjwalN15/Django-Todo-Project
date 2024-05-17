from django.db import models

# Create your models here.

class Todo_Table(models.Model):
    Name = models.CharField(max_length=200)
    Description = models.TextField()
    Status = models.CharField(max_length=200)