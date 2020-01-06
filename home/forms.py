from django.forms import ModelForm
from .models import LOP10, THPTQG

class PostLop10Form(ModelForm):
    class Meta:
        model = LOP10
        fields = ['Exam_id','Number','Question','A','B','C','D','Answer']

class PostTHPTQGForm(ModelForm):
    class Meta:
        model = THPTQG
        fields = ['Exam_id','Number','Question','A','B','C','D','Answer']