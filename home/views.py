from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.views import View
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User, auth
from django.contrib.admin.forms import AdminPasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from .forms import Lop10Form, ThptgqForm, ExamForm, Lop10Formset, ThptqgFormset, ResultForm
from django.forms import modelformset_factory, inlineformset_factory, formset_factory
from .models import LOP10, THPTQG, Exam, Result
from django.urls import reverse_lazy, reverse
from django.db import transaction
from django.http import HttpResponseRedirect
from django.db import models







# Account related, front

def index(request):
	return render(request, 'pages/home.html')


def choose(request):
	return render(request, 'pages/choose-thptqg.html')


def viewAccount(request):
    return render(request, 'pages/profile.html')

def editAccount(request):
    return render(request,'pages/editAccount.html')

def updateAccount(request,id):
   user = User.objects.get(id =id)
   user.first_name= request.POST.get('first_name')
   user.last_name = request.POST.get('last_name')
   user.username = request.POST.get('username')
   user.email = request.POST.get('email')
   user.save()
   return render(request, 'pages/profile.html', {'user': user})


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
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		username = request.POST.get('username')
		email = request.POST.get('email')
		password = request.POST.get('password')
		user = User.objects.create_user(
			first_name = first_name, last_name = last_name, username = username, email = email, password = password)
		user.save()
		print('User created')
		return redirect('/login')
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
	if request.user.is_authenticated:
		questions = Exam.objects.filter(Type = "Lop 10")
		return render(request, 'pages/lop10.html', {'questions':questions})
	else: 
		return HttpResponse("Moi ban dang nhap")

def detail_Lop10(request,Exam_id):
	lop10 = LOP10.objects.filter(Exam_id = int(Exam_id))
	thptqg = THPTQG.objects.filter(Exam_id = int(Exam_id))
	context = {
		'Exam_id':Exam_id,
		'lop10':lop10,
		'thptqg':thptqg,
	}
	return render(request, 'pages/exam.html', context)

def viewTHPTQG(request):
	if request.user.is_authenticated:
		questions = Exam.objects.filter(Type = "THPT")
		return render(request, 'pages/thptqg.html', {'questions':questions})
	else: 
		return HttpResponse("Moi ban dang nhap")

def detail_THPTQG(request,Exam_id):
	lop10 = LOP10.objects.filter(Exam_id = int(Exam_id))
	thptqg = THPTQG.objects.filter(Exam_id = int(Exam_id))
	context = {
		'Exam_id':Exam_id,
		'lop10':lop10,
		'thptqg':thptqg,
	}
	return render(request, 'pages/exam_thptqg.html', context)



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
		exam = LOP10.objects.get(id = Exam_id)
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
   return redirect('manage')



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


def exam_detail(request,Exam_id):
	lop10 = LOP10.objects.filter(Exam_id = int(Exam_id))
	thptqg = THPTQG.objects.filter(Exam_id = int(Exam_id))
	context = {
		'Exam_id':Exam_id,
		'lop10':lop10,
		'thptqg':thptqg,
	}
	return render(request, 'pages/exam.html', context)


class ExamForLop10(LoginRequiredMixin,View):

	def get(self,request,Exam_id):
		if Exam.objects.filter(Type = "Lop 10"):
			lop10 = LOP10.objects.filter(Exam_id = int(Exam_id))
			context = {
				'Exam_id':Exam_id,
				'lop10':lop10,
			}
			return render(request, 'pages/thi_lop10.html', context)


	def post(self,request,Exam_id):
		grade = 0
		rs=0
		if Exam.objects.filter(Type = "Lop 10"):
			lop10 = LOP10.objects.filter(Exam_id = int(Exam_id))
			for i in lop10:
				for key in request.POST:
					try:
						key=int(key)
					except ValueError:
						continue
					if i.id == key:
						for j in request.POST[f"{key}"]:
							dapan = LOP10.objects.filter(id=int(key)).values()
							if i.Answer == j:
								grade=1
								rs+=1
							else:
								grade=0
							result = Result(
								User = request.user,
								Exam = Exam.objects.get(id = int(Exam_id)),
								question_lop10 = LOP10.objects.get(id=i.id),
								choice = j,
								grade = grade,
							)
							result.save()
			return render(request,'pages/exam_result_lop10.html', {'Exam_id':Exam_id,'rs':rs,'lop10':lop10})


# class ExamForTHPT(LoginRequiredMixin,View):

# 	def get(self,request,Exam_id):
# 		if Exam.objects.filter(Type = "THPT"):
# 			thptqg = THPTQG.objects.filter(Exam_id = int(Exam_id))
# 			context = {
# 				'Exam_id':Exam_id,
# 				'thptqg':thptqg,
# 			}
# 			return render(request, 'pages/thi_thpt.html', context)

# 	def post(self,request,Exam_id):
# 		grade=0
# 		rs=0
# 		if Exam.objects.filter(Type = "THPT"):
# 			thptqg = THPTQG.objects.filter(Exam_id = int(Exam_id))
# 			for i in thptqg:
# 				for key in request.POST:
# 					try:
# 						key=int(key)
# 					except ValueError:
# 						continue
# 					if i.id == key:
# 						for j in request.POST[f"{key}"]:
# 							dapan = THPTQG.objects.filter(id=int(key)).values()
# 							if i.Answer == j:
# 								grade=1
# 								rs+=1
# 							else:
# 								grade=0
# 							result = Result(
# 								User = request.user,
# 								Exam = Exam.objects.get(id = int(Exam_id)),
# 								question_thpt = THPTQG.objects.get(id=i.id),
# 								choice = j,
# 								grade = grade,
# 							)
# 							result.save()
# 			return render(request,'pages/exam_result_thpt.html', {'Exam_id':Exam_id,'rs':rs,'thptqg':thptqg})

def exam_delete(request,pk):
	obj = get_object_or_404(Exam, pk=int(pk))
	if request.method == 'POST':
		obj.delete()
		return redirect('manage')
	return render(request, 'manage', {'object':obj})


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
