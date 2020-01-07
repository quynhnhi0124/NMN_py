from django.forms import ModelForm

# from .models import Question, THPTQG
from .models import LOP10, THPTQG


class PostLop10Form(ModelForm):
    class Meta:
        model = LOP10
        fields = ['Exam','Question','A','B','C','D','Answer']

class PostTHPTQGForm(ModelForm):
    class Meta:
        model = THPTQG
        fields = ['Exam','Question','A','B','C','D','Answer']
