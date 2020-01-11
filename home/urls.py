from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth.views import PasswordResetView
from .views import ExamCreate, Exam, AddQuestionThptqg, AddQuestionLop10


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
    path('editAccount/',views.editAccount,name="editAccount"),


    path('manage/add/', ExamCreate.as_view(), name = "add_exam" ),

    path('manage/add_question/thptqg/<int:Exam_id>/', views.AddQuestionThptqg, name = "add_question_thpt"),
    path('manage/add_question/lop10/<int:Exam_id>/', views.AddQuestionLop10, name = "add_question_lop10"),

   path('edit_question_lop10/<int:Exam_id>/<int:id>',views.editQuestionLop10, name = "edit_question_lop10" ),
    path('update_question_lop10/<int:Exam_id>/<int:id>/',views.updateQuestionLop10, name = "update_question_lop10" ),
    path('delete_question_lop10/<int:Exam_id>/<int:id>/',views.deleteQuestionLop10, name = "delete_question_lop10" ),

    path('edit_question_thptqg/<int:Exam_id>',views.editQuestionTHPTQG, name = "edit_question_thptqg" ),
    path('update_question_thptqg/<int:Exam_id>',views.updateQuestionTHPTQG, name = "update_question_thptqg" ),
    path('delete_question_thptqg/<int:Exam_id>',views.deleteQuestionTHPTQG, name = "delete_question_thptqg" ),

 

    path('manage/add_question/thptqg/<int:Exam_id>/', views.AddQuestionThptqg, name = "add_question_thptqg"),
  
    path('exam_detail/<int:Exam_id>/', views.exam_detail, name = "exam_detail"),


    path('manage/delete/<int:pk>/',views.exam_delete, name = 'exam_delete'),

    # reset password
    path('password_reset/', PasswordResetView.as_view(), name = 'password_reset'),

    path('lam-bai-thi/<int:Exam_id>/', views.Examm.as_view(), name ='vaothi'),


    # path('update/',views.updateUserView,name="update"),
    # path('delete/',views.deleteUserView,name="delete"),
    path('viewthptqg/',views.viewTHPTQG, name = 'viewthptqg'),
    path('detail_thptqg/<int:Exam_id>/', views.detail_THPTQG, name = "detail_thptqg"),
    path('viewlop10/',views.viewLop10, name = 'viewlop10'),
    path('detail_lop10/<int:Exam_id>/', views.detail_Lop10, name = "detail_lop10"),


]