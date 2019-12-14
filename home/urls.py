from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth.views import PasswordResetView
from .views import addQuestion


urlpatterns = [
    path('home/',views.index, name = 'home'),
    path('choose-your-exam/',views.choose, name = 'choose-your-exam'),
    path('thptqg/',views.thptqg, name = 'thptqg'),

    # login and signin
    path('login/',views.loginView, name = "login"),
    path('register/',views.registerView, name = "register"),
    path('logout/',views.logoutView, name = "logout"),
    path('manage/',views.manageView, name = "manage"),
    path('add/', addQuestion.as_view(), name = "add_question" ),
    path('edit/<int:id>',views.editDataQuestion, name = "edit_question" ),
    path('update/<int:id>',views.updateDataQuestion, name = "update_question" ),
    path('delete/<int:id>',views.deleteDataQuestion, name = "delete_question" ),
    
    # reset password
    path('password_reset/', PasswordResetView.as_view(), name = 'password_reset'),

    path('edit/',views.editUserView,name="edit"),
    # path('update/',views.updateUserView,name="update"),
    # path('delete/',views.deleteUserView,name="delete"),
    path('detail/',views.detailView, name = "detail"),
    path('start/',views.viewQuestion, name = "start"),


]