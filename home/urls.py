from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth.views import PasswordResetView
from .views import ExamCreate, AddQuestionLop10, AddQuestionThptqg, updateDataQuestion


urlpatterns = [
    path('home/',views.index, name = 'home'),
    path('choose-thptqg/',views.choose, name = 'choose-thptqg'),

    path('choose-your-exam/',views.choose, name = 'choose-your-exam'),
    

    # login and signin
    path('login/',views.loginView, name = "login"),
    path('register/',views.registerView, name = "register"),
    path('logout/',views.logoutView, name = "logout"),
    path('profile/',views.viewAccount, name = 'profile'),
    path('manage/',views.manageView, name = "manage"),
    path('editAccount/',views.viewEditAccount,name="editAccount"),


    path('manage/add/', ExamCreate.as_view(), name = "add_exam" ),
    path('manage/add_question/lop-10/<int:Exam_id>/', views.AddQuestionLop10, name = "add_question_lop10"),
    path('manage/add_question/thptqg/<int:Exam_id>/', views.AddQuestionThptqg, name = "add_question_thptqg"),
    path('edit/<int:id>',views.editDataQuestion, name = "edit_question" ),
    path('update/<int:id>',views.updateDataQuestion, name = "update_question" ),
    path('delete/<int:id>',views.deleteDataQuestion, name = "delete_question" ),
    path('detail/',views.detailView, name = "detail"),
    path('exam_detail/<int:Exam_id>/', views.exam_detail, name = "exam_detail"),

    path('manage/delete/<int:pk>/',views.exam_delete, name = 'exam_delete'),

    # reset password
    path('password_reset/', PasswordResetView.as_view(), name = 'password_reset'),

    # path('edit/',views.editUserView,name="edit"),

    # path('update/',views.updateUserView,name="update"),
    # path('delete/',views.deleteUserView,name="delete"),
    path('viewthptqg/',views.viewTHPTQG, name = 'viewthptqg'),
    path('viewlop10/',views.viewLop10, name = 'viewlop10'),


]