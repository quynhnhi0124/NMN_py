from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.
def index(request):
    return render(request, 'pages/home.html')

def choose(request):
    return render(request, 'pages/choose-your-exam.html')

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
		email=request.POST['email']
		password=request.POST['password']
		user=User.objects.create_user(username=username,email=email,password=password)
		user.save()
		print('User created')
		return redirect('/home/login')
	else:
		return render(request,'pages/register.html')

def logoutView(request):
	auth.logout(request)
	return render(request,'pages/home.html')