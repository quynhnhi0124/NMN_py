from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class LOP10(models.Model):
    # Exam_id = models.ForeignKey(Exam_id, max_length=11, on_delete=models.CASCADE, null=True, blank=True)
    Exam_id = models.IntegerField()
    Number = models.IntegerField()
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
<<<<<<< HEAD
    # Exam_id = models.ForeignKey(Exam_id, max_length=11, on_delete=models.CASCADE, null=True, blank=True)
    Exam_id = models.IntegerField()
    Number = models.IntegerField()
=======
    STT = models.IntegerField()

>>>>>>> 3ec7293f04393518e858d7bd04ce07cccd6cf9ae
    Question = models.TextField()
    A = models.CharField(max_length=5000)
    B = models.CharField(max_length=5000)
    C = models.CharField(max_length=5000)
    D = models.CharField(max_length=5000)
    Answer = models.CharField(max_length=1)

def __str__(self):
    return self.THPTQG

    return self.THPTQG

