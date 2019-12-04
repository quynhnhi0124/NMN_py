from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='home'),
    path('choose-your-exam/',views.choose, name='choose-your-exam')
]