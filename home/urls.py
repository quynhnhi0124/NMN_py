from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth.views import PasswordResetView
from .views import ExamCreate, Exam, AddQuestionThptqg, AddQuestionLop10


urlpatterns = [
    #base
    path('home/',views.index, name = 'home'),
    path('choose-thptqg/',views.choose, name = 'choose-thptqg'),
    path('choose-your-exam/',views.choose, name = 'choose-your-exam'),
    path('viewthptqg/',views.viewTHPTQG, name = 'viewthptqg'),
    path('viewlop10/',views.viewLop10, name = 'viewlop10'),
    # login and signin, profile
    path('login/',views.loginView, name = "login"),
    path('register/',views.registerView, name = "register"),
    path('logout/',views.logoutView, name = "logout"),
    path('profile/',views.viewAccount, name = 'profile'),
    path('editAccount/',views.editAccount,name="editAccount"),
    path('updateAccount/<int:id>',views.updateAccount,name="updateAccount"),
    #for superuser, add, update, delete
    path('manage/',views.manageView, name = "manage"),
    path('manage/add/', ExamCreate.as_view(), name = "add_exam" ),
    path('manage/add_question/thptqg/<int:Exam_id>/', views.AddQuestionThptqg, name = "add_question_thpt"),
    path('manage/add_question/lop10/<int:Exam_id>/', views.AddQuestionLop10, name = "add_question_lop10"),
    path('manage/add_question/thptqg/<int:Exam_id>/', views.AddQuestionThptqg, name = "add_question_thptqg"),
    path('manage/delete/<int:pk>/',views.exam_delete, name = 'exam_delete'),
    path('edit_question_lop10/<int:Exam_id>/<int:id>',views.editQuestionLop10, name = "edit_question_lop10" ),
    path('edit_question_thptqg/<int:Exam_id>',views.editQuestionTHPTQG, name = "edit_question_thptqg" ),
    path('update_question_lop10/<int:Exam_id>/<int:id>',views.updateQuestionLop10, name = "update_question_lop10" ),
    path('update_question_thptqg/<int:Exam_id>/',views.updateQuestionTHPTQG, name = "update_question_thptqg" ),
    #exam
    path('exam_detail/<int:Exam_id>/', views.exam_detail, name = "exam_detail"),
    path('detail_thptqg/<int:Exam_id>/', views.detail_THPTQG, name = "detail_thptqg"),
    path('detail_lop10/<int:Exam_id>/', views.detail_Lop10, name = "detail_lop10"),
    path('lam-bai-thi/lop10/<int:Exam_id>/', views.ExamForLop10.as_view(), name ='vaothi-lop10'),
    path('ket-qua-thi/lop10/<int:Exam_id>/',views.ExamForLop10.as_view(), name = 'ket-qua-thi-lop10'),
    # path('lam-bai-thi/thptqg/<int:Exam_id>/', views.ExamForTHPT.as_view(), name ='vaothi-thpt'),
    # path('ket-qua-thi/thptqg/<int:Exam_id>/',views.ExamForTHPT.as_view(), name = 'ket-qua-thi-thpt'),


]