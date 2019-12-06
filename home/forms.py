from django.forms import ModelForm
from .models import Question

class PostQuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['STT','Question','A','B','C','D','Answer']