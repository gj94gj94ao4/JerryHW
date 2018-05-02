from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.CharField(max_length=200, blank=True)
    title = models.CharField(max_length=200, blank=True)
    text = models.TextField()
    
    def __str__(self):
        return self.title
