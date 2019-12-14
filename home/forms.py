from django.forms import ModelForm
from .models import Question, THPTQG

class PostQuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['STT','Question','A','B','C','D','Answer']

class PostTHPTQGForm(ModelForm):
    class Meta:
        model = Question
        fields = ['STT','Question','A','B','C','D','Answer']