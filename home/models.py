from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class LOP10(models.Model):
    STT = models.IntegerField()
    Question = models.TextField()
    A = models.CharField(max_length=5000)
    B = models.CharField(max_length=5000)
    C = models.CharField(max_length=5000)
    D = models.CharField(max_length=5000)
    Answer = models.CharField(max_length=1)

def __str__(self):
    return self.Question


class THPTQG(models.Model):
    Code = models.IntegerField()

    return self.LOP10

class THPTQG(models.Model):
    STT = models.IntegerField()

    Question = models.TextField()
    A = models.CharField(max_length=5000)
    B = models.CharField(max_length=5000)
    C = models.CharField(max_length=5000)
    D = models.CharField(max_length=5000)
    Answer = models.CharField(max_length=1)

def __str__(self):
    return self.THPTQG

    return self.THPTQG

