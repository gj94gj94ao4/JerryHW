from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    birthday = models.CharField(max_length=15)
    sex = models.CharField(max_length=15)
    def __str__(self):
        return self.name
