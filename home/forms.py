from django.forms import ModelForm, modelformset_factory, BaseFormSet, inlineformset_factory
from .models import Lop10, Thptqg, Exam
from django import forms

class Lop10Form(ModelForm):
    class Meta:
        model = Lop10
        fields = ['Question','A','B','C','D','Answer']


class ThptgqForm(ModelForm):
    class Meta:
        model = Thptqg
        fields = ['Question','A','B','C','D','Answer']


class ExamForm(ModelForm):
    select = (
        ('Lop 10', 'Lop 10'),
        ('THPT', 'THPT'),
    )
    Type = forms.ChoiceField(choices = select)
    class Meta():
        model = Exam
        fields = ['Name','Type']


Lop10Formset = inlineformset_factory(Exam, Lop10,fields=('id','Question','A','B','C','D','Answer'),can_delete=False,max_num=10)
ThptqgFormset = inlineformset_factory(Exam, Thptqg,fields=('id','Question','A','B','C','D','Answer'),can_delete=False,max_num=10)

