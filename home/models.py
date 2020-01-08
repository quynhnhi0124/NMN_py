from django.db import models

# Create your models here.
from django.db import models
# Create your models here.
class Exam(models.Model):

    Name = models.CharField(max_length=100)
    Type = models.CharField(max_length=25, null=True)

    # def get_absolute_url(self):
    #     return reverse('add_question', kwargs = {'pk' : self.pk})

    def __str__(self):
        return self.Name

class Lop10(models.Model):
    
    Exam = models.ForeignKey(Exam,max_length=11, on_delete=models.CASCADE, null=True, blank=True)
    Question = models.TextField()
    A = models.CharField(max_length=3000)
    B = models.CharField(max_length=3000)
    C = models.CharField(max_length=3000)
    D = models.CharField(max_length=3000)
    Answer = models.CharField(max_length=1)

    def __str__(self):
        return self.Question

    # def exam_name(self): 
    #     return self.exam.id
    # exam_name.short_description = "Exam_Name"

class Thptqg(models.Model):
    
    Exam = models.ForeignKey(Exam,max_length=11, on_delete=models.CASCADE, null=True, blank=True)
    Question = models.TextField()
    A = models.CharField(max_length=3000)
    B = models.CharField(max_length=3000)
    C = models.CharField(max_length=3000)
    D = models.CharField(max_length=3000)
    Answer = models.CharField(max_length=1)

    def __str__(self):
        return self.Question

    # def exam_name(self): 
    #     return self.exam.id
    # exam_name.short_description = "Exam_Name"
    
    # from django.contrib.auth.models import User
    # from PIL import Image
