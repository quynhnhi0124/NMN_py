from django.forms import ModelForm

from .models import Question, THPTQG
from .models import LOP10, THPTQG


class PostLop10Form(ModelForm):
    class Meta:

        model = Question
        fields = ['STT','Question','A','B','C','D','Answer']


class PostTHPTQGForm(ModelForm):
    class Meta:
        model = THPTQG
        fields = ['Question','A','B','C','D']

        model = LOP10
        fields = ['Exam_id','Number','Question','A','B','C','D','Answer']

class PostTHPTQGForm(ModelForm):
    class Meta:
        model = THPTQG
<<<<<<< HEAD
        fields = ['Exam_id','Number','Question','A','B','C','D','Answer']
=======
        fields = ['STT','Question','A','B','C','D','Answer']

>>>>>>> 3ec7293f04393518e858d7bd04ce07cccd6cf9ae
