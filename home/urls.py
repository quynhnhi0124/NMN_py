from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='home'),
    path('choose-your-exam/',views.choose, name='choose-your-exam'),
    path('login/',views.loginView,name="login"),
    path('register/',views.registerView,name="register"),
    path('logout/',views.logoutView,name="logout"),

]