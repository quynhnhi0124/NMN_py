from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='home'),
    path(r'^$',views.choose, name='choose-your-exam')
]