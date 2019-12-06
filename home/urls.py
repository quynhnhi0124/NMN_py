from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth.views import PasswordResetView
from .views import addQuestion


urlpatterns = [
    path('home/',views.index, name = 'home'),
    path('choose-your-exam/',views.choose, name = 'choose-your-exam'),

    # login and signin
    path('login/',views.loginView, name = "login"),
    path('register/',views.registerView, name = "register"),
    path('logout/',views.logoutView, name = "logout"),
    path('manage/',views.manageView, name = "manage"),
    path('add/', addQuestion.as_view(), name = "add_question" ),
    # reset password
    path('password_reset/', PasswordResetView.as_view(), name = 'password_reset')

]