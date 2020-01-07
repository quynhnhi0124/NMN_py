from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User,auth
from django.contrib.admin.forms import AdminPasswordChangeForm
from django.contrib.auth.views import PasswordChangeView

from .forms import PostQuestionForm
from .forms import PostTHPTQGForm
from .models import Question, THPTQG

from .forms import PostLop10Form, PostTHPTQGForm
from .models import LOP10, THPTQG





# Create your views here.
def index(request):
    return render(request, 'pages/home.html')

def choose(request):
    return render(request, 'pages/choose-thptqg.html')

def thptqg(request):
	thptqg = THPTQG.objects.only("Question","A","B","C","D")
	return render(request, 'pages/thptqg.html', {'thptqg':thptqg})

def loginView(request):
	if request.method == 'POST':
		username=request.POST['username']
		password=request.POST['password']

		user=auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request,user)
			return redirect("/home")
		else:
			messages.info(request,'invalid credentials')
			return redirect("login")
	else:
	
		return render(request,'pages/login.html')

def registerView(request):
	if request.method=='POST':
		username=request.POST['username']
		first_name=request.POST['first_name']
		last_name=request.POST['last_name']
		email=request.POST['email']
		password=request.POST['password']
		user=User.objects.create_user(username=username,email=email,password=password,first_name=first_name,last_name=last_name)
		user.save()
		print('User created')
		return redirect('/home/login')
	else:
		return render(request,'pages/register.html')

def logoutView(request):
	auth.logout(request)
	return render(request,'pages/home.html')

class addQuestion(LoginRequiredMixin,View):
	login_url = '/login/'
	def get(self, request):
		if request.user.is_superuser:
			frm = PostQuestionForm()
			context = {'form':frm}
			return render(request, 'pages/add.html', context)
		else:
			return redirect("home")
	def post(self,request):
		frm = PostQuestionForm(request.POST)
		# if request.user.has_perm('home.add_question'):
		frm.save()
		return HttpResponse("Them cau hoi thanh cong")

def viewAccount(request):
    return render(request, 'pages/profile.html')


def viewLop10(request):
	questions = LOP10.objects.all()
	return render(request, 'pages/lop10.html', {'questions':questions})

def viewTHPTQG1(request):
	questions = THPTQG.objects.filter(Exam_id=1)
	return render(request, 'pages/thptqg1.html', {'questions':questions})

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


def deleteDataQuestion(request, id):
   question = Question.objects.get(id = id)
   question.delete()
   return redirect('start')

def manageView(request):
	if request.user.is_superuser:
		return render(request,'pages/manage.html')
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

