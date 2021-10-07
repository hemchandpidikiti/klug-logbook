from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('attendence/', views.attendence, name='attendence'),
    path('changepwd/', views.changepwd, name='changepwd'),
    path('bydate/', views.bydate, name='bydate'),
    path('id/', views.id, name='id'),
    path('register', views.register, name='register')
]