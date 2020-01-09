from django.forms import ModelForm, modelformset_factory, BaseFormSet, inlineformset_factory
from .models import LOP10, THPTQG, Exam,KetQuaDuThi
from django import forms

class Lop10Form(ModelForm):
    class Meta:
        model = LOP10
        fields = ['Question','A','B','C','D','Answer']


class ThptgqForm(ModelForm):
    class Meta:
        model = THPTQG
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

class KetQuaDuThiForm(ModelForm):
    class Meta:
        model = KetQuaDuThi
        fields = ['username','email','result','Exam','Type']

Lop10Formset = inlineformset_factory(Exam, LOP10,fields=('id','Question','A','B','C','D','Answer'),can_delete=False,max_num=10)
ThptqgFormset = inlineformset_factory(Exam, THPTQG,fields=('id','Question','A','B','C','D','Answer'),can_delete=False,max_num=10)

