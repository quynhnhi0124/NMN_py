from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.views import View
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User, auth
from django.contrib.admin.forms import AdminPasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from .forms import Lop10Form, ThptgqForm, ExamForm, Lop10Formset, ThptqgFormset
from django.forms import modelformset_factory, inlineformset_factory, formset_factory
from .models import LOP10, THPTQG, Exam
from django.urls import reverse_lazy, reverse
from django.db import transaction
from django.http import HttpResponseRedirect





# Create your views here.
def index(request):
	return render(request, 'pages/home.html')


def choose(request):
	return render(request, 'pages/choose-thptqg.html')


def viewAccount(request):
    return render(request, 'pages/profile.html')


def loginView(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			return redirect("/home")
		else:
			messages.info(request, 'invalid credentials')
			return redirect("login")
	else:

		return render(request, 'pages/login.html')


def registerView(request):
	if request.method == 'POST':
		username = request.POST['username']
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		password = request.POST['password']
		user = User.objects.create_user(
			username=username, email=email, password=password, first_name=first_name, last_name=last_name)
		user.save()
		print('User created')
		return redirect('/home/login')
	else:
		return render(request, 'pages/register.html')


def logoutView(request):
	auth.logout(request)
	return render(request, 'pages/home.html')


class ExamCreate(LoginRequiredMixin,View):
	login_url = '/login/'

	def get(self, request):
		if request.user.is_superuser:
			add_exam = ExamForm()
			return render(request, 'pages/add_exam.html', {'add_exam': add_exam})
		else:
			return redirect('home')


	def post(self,request):
		add_exam = ExamForm(request.POST)
		if add_exam.is_valid():
			add_exam.save()
			return redirect('manage')
		else:
			errors = exam.errors
			print(errors)
			return HttpResponse("That bai")


def AddQuestionLop10(request,Exam_id):
	print("Exam_id lop 10", Exam_id)
	exam = Exam.objects.get(pk=int(Exam_id))
	Lop10InlineFormset = inlineformset_factory(Exam, LOP10,fields=('Question','A','B','C','D','Answer'),can_delete=False,max_num=10, extra=10)
	if request.method == 'POST':
		formset = Lop10InlineFormset(request.POST, request.FILES, instance=exam)
		print (format)
		if formset.is_valid():
			
			formset.save()
			return redirect('add_question/lop-10/',Exam_id=Exam_id)
		else:
			errors = formset.errors
			print(errors)
	else:
		formset = Lop10InlineFormset(instance=exam)
		return render(request, 'pages/add_question.html', {'formset':formset,'Exam_id':Exam_id})


def AddQuestionThptqg(request,Exam_id):
	print("aaaaaaaaa")
	print("Exam_id thptqg", Exam_id)
	exam = Exam.objects.get(pk=int(Exam_id))
	ThptqgInlineFormset = inlineformset_factory(Exam, THPTQG,fields=('Question','A','B','C','D','Answer'),can_delete=False,max_num=10, extra=10)
	if request.method == 'POST':
		formset = ThptqgInlineFormset(request.POST, request.FILES, instance=exam)
		print (format)
		if formset.is_valid():
			
			formset.save()
			return redirect('add_question/thptqg/',Exam_id=Exam_id)
		else:
			errors = formset.errors
			print(errors)
	else:
		formset = ThptqgInlineFormset(instance=exam)
		return render(request, 'pages/add_question.html', {'formset':formset,'Exam_id':Exam_id})


def viewLop10(request):
	questions = LOP10.objects.all()
	return render(request, 'pages/lop10.html', {'questions':questions})

def viewTHPTQG(request):
	questions = THPTQG.objects.all()
	return render(request, 'pages/thptqg.html', {'questions':questions})

def editDataQuestion(request,id):
	if request.user.is_superuser:
		question =Question.objects.get(id=id)
		return render(request,'pages/detail.html',{'question':question})
	else:
		return redirect("home")
def updateDataQuestion(request, id):
   question = Question.objects.get(id = id)
   question.Question = request.POST.get('Question')
   question.A = request.POST.get('A')
   question.B = request.POST.get('B')
   question.C = request.POST.get('C')
   question.D = request.POST.get('D')
   question.Answer = request.POST.get('Answer')
   question.save()
   return redirect("start")


def exam_delete(request,pk):
	obj = get_object_or_404(Exam, pk=int(pk))
	if request.method == 'POST':
		obj.delete()
		return redirect('manage')
	return render(request, 'manage', {'object':obj})

def deleteDataQuestion(request, id):
   question = Question.objects.get(id = id)
   question.delete()
   return redirect('start')

# def exam_detail(request):
# 	exam_name = Exam.objects.values('Type')
# 	for name in exam_name:
# 		if name == 'Lop 10':



def manageView(request):
	if request.user.is_superuser:
		exam = Exam.objects.all()
		return render(request, 'pages/manage.html', {'exam':exam})
	else:
		return redirect("home")

# def password_changed(password ,user = None , password_validators = None):
# 	if password_validators is None :
# 		password_validators = get_default_validators()
# 	for validator in password_validators:
# 		password_changed = getattr(validator,'password_changed', lambda *a: None)
# 		password_changed(password,user)
def viewEditAccount(request):
    return render(request,'pages/editAccount.html')

def detailView(request):
    return render(request,'pages/detail.html')

def editUserView(request):
	return render(request, 'pages/editUser.html')
