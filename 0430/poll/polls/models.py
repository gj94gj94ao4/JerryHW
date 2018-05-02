from django.db import models

# Create your models here.

class Pool(models.Model):
    poolName = models.CharField(max_length=200)

    def __str__(self):
        return self.poolName

class Choice(models.Model):
    pool = models.ForeignKey(Pool)
    choiceName = models.CharField(max_length=50)
    chount = models.IntegerField()

    def __str__(self):
        return self.choiceName
