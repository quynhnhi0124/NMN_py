from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Exam(models.Model):

    Name = models.CharField(max_length=100)
    Type = models.CharField(max_length=25, null=True)

    # def get_absolute_url(self):
    #     return reverse('add_question', kwargs = {'pk' : self.pk})

    def __str__(self):
        return self.Name


class LOP10(models.Model):

    Exam= models.ForeignKey(Exam,max_length=11, on_delete=models.CASCADE, null=True, blank=True)
    Question = models.TextField()
    A = models.CharField(max_length=5000)
    B = models.CharField(max_length=5000)
    C = models.CharField(max_length=5000)
    D = models.CharField(max_length=5000)
    Answer = models.CharField(max_length=1)

    def __str__(self):
        return self.Question

class THPTQG(models.Model):

    Exam = models.ForeignKey(Exam,max_length=11, on_delete=models.CASCADE, null=True, blank=True)
    Question = models.TextField()
    A = models.CharField(max_length=5000)
    B = models.CharField(max_length=5000)
    C = models.CharField(max_length=5000)
    D = models.CharField(max_length=5000)
    Answer = models.CharField(max_length=1)

    def __str__(self):
        return self.Question

class Result(models.Model):
    User = models.ForeignKey(User, max_length = 11, on_delete = models.CASCADE, null = True, blank =True)
    Exam = models.ForeignKey(Exam,max_length=11, on_delete=models.CASCADE, null=True, blank=True)
    question_lop10 = models.ForeignKey(LOP10,max_length=11, on_delete=models.CASCADE, null=True, blank=True)
    question_thpt = models.ForeignKey(THPTQG,max_length=11, on_delete=models.CASCADE, null=True, blank=True)
    choice = models.TextField(max_length = 100)
    grade = models.IntegerField()
     def __str__(self):
        return self.Exam
