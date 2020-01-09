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
from .models import LOP10, THPTQG, Exam,KetQuaDuThi
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

def editAccount(request):
    return render(request,'pages/editAccount.html')

def updateAccount(request, id):
   question = User.objects.get(id = id)
   question.first_name = request.POST.get('first_name')
   question.last_name = request.POST.get('last_name')
   question.username = request.POST.get('username')
   question.email = request.POST.get('email')
   question.save()
   return redirect("manage")


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


def viewLop10(request):
	questions = Exam.objects.filter(Type = "Lop 10")
	return render(request, 'pages/lop10.html', {'questions':questions})

def detail_Lop10(request,Exam_id):
	lop10 = LOP10.objects.filter(Exam_id = int(Exam_id))
	thptqg = THPTQG.objects.filter(Exam_id = int(Exam_id))
	context = {
		'Exam_id':Exam_id,
		'lop10':lop10,
		'thptqg':thptqg,
	}
	return render(request, 'pages/exam.html', context)

def AddQuestionLop10(request,Exam_id):
	print("Exam_id lop 10", Exam_id)
	exam = Exam.objects.get(pk=int(Exam_id))
	Lop10InlineFormset = inlineformset_factory(Exam, LOP10,fields=('Question','A','B','C','D','Answer'),can_delete=False,max_num=10, extra=10)
	if request.method == 'POST':
		formset = Lop10InlineFormset(request.POST, request.FILES, instance=exam)
		if formset.is_valid():
			formset.save()
			return redirect('manage')
		else:
			errors = formset.errors
			print(errors)
	else:
		formset = Lop10InlineFormset(instance=exam)
		return render(request, 'pages/add_question_lop10.html', {'formset':formset,'Exam_id':Exam_id})


def editQuestionLop10(request,Exam_id,id):
	if request.user.is_superuser:
		question=LOP10.objects.get(id=id)
		exam = Exam.objects.get(id = Exam_id)
		return render(request,'pages/editQuestion.html',{'question':question , 'exam':exam})
	else:
		return redirect("home")


def updateQuestionLop10(request,id, Exam_id):
   question = LOP10.objects.get(id =id)
   question.Question = request.POST.get('Question')
   question.A = request.POST.get('A')
   question.B = request.POST.get('B')
   question.C = request.POST.get('C')
   question.D = request.POST.get('D')
   question.Answer = request.POST.get('Answer')
   question.save()
   exam = LOP10.objects.get(id = Exam_id)
   return render(request, 'pages/exam.html', {'Exam_id':Exam_id})


def deleteQuestionLop10(request,Exam_id,id):
   question = LOP10.objects.get(id=id)
   exam = LOP10.objects.get(id = Exam_id)
   question.delete()
   return redirect('home')


def viewTHPTQG(request):
	questions = Exam.objects.filter(Type = "THPT")
	return render(request, 'pages/thptqg.html', {'questions':questions})


def AddQuestionThptqg(request,Exam_id):
	print("aaaaaaaaa")
	print("Exam_id thptqg", Exam_id)
	exam = Exam.objects.get(pk=int(Exam_id))
	ThptqgInlineFormset = inlineformset_factory(Exam, THPTQG,fields=('Question','A','B','C','D','Answer'),can_delete=False,max_num=10, extra=10)
	if request.method == 'POST':
		formset = ThptqgInlineFormset(request.POST, request.FILES, instance=exam)
		if formset.is_valid():
			
			formset.save()
			return redirect('manage')
		else:
			errors = formset.errors
			print(errors)
	else:
		formset = ThptqgInlineFormset(instance=exam)
		return render(request, 'pages/add_question_thptqg.html', {'formset':formset,'Exam_id':Exam_id})



def editQuestionTHPTQG(request,Exam_id):
	if request.user.is_superuser:
		question=THPTQG.objects.get(id=Exam_id)
		return render(request,'pages/editQuestion.html',{'question':question})
	else:
		return redirect("home")


def updateQuestionTHPTQG(request, Exam_id):
   question = THPTQG.objects.get(id = Exam_id)
   question.Question = request.POST.get('Question')
   question.A = request.POST.get('A')
   question.B = request.POST.get('B')
   question.C = request.POST.get('C')
   question.D = request.POST.get('D')
   question.Answer = request.POST.get('Answer')
   question.save()
   return redirect("home")

def deleteQuestionTHPTQG(request, id):
   question = THPTQG.objects.get(id = id)
   question.delete()
   return redirect('viewlop10')


def exam_detail(request,Exam_id):
	# exam_id = Exam.objects.get(pk = int(id))
	lop10 = LOP10.objects.filter(Exam_id = int(Exam_id))
	thptqg = THPTQG.objects.filter(Exam_id = int(Exam_id))
	context = {
		'Exam_id':Exam_id,
		'lop10':lop10,
		'thptqg':thptqg,
	}
	return render(request, 'pages/exam.html', context)


def exam_delete(request,pk):
	obj = get_object_or_404(Exam, pk=int(pk))
	if request.method == 'POST':
		obj.delete()
		return redirect('manage')
	return render(request, 'manage', {'object':obj})



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

# def editUserView(request):
# 	return render(request, 'pages/editUser.html')
