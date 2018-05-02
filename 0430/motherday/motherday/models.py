from django.db import models

# Create your models here.

class Post(models.Model):
    auther = models.CharField(max_length=20, blank=True)
    text = models.TextField()

    def __str__(self):
        return self.auther