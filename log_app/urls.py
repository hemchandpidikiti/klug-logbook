from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('attendence/', views.attendence, name='attendence'),
    path('changepwd/', views.changepwd, name='changepwd'),
    path('bydate/', views.bydate, name='bydate'),
    path('id/', views.id, name='id'),
    path('print/', views.print, name='print'),
    path('intimate/', views.intimate, name='intimate'),
    path('accounts/register/', views.register, name='register'),
    path('accounts/login/', views.auth_login, name='auth_login')
]