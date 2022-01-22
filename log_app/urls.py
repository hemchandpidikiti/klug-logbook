from django.urls import path, include
from . import views
from .views import MasterViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('master', MasterViewSet, 'master')

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include(router.urls)),
    path('attendence/', views.attendence, name='attendence'),
    path('changepwd/', views.changepwd, name='changepwd'),
    path('bydate/', views.bydate, name='bydate'),
    path('id/', views.id, name='id'),
    path('print/', views.data_print, name='data_print'),
    path('intimate/', views.intimate, name='intimate'),
    path('card_reg/', views.card_registrations, name='card_registrations'),
    path('accounts/register/', views.register, name='register'),
    path('accounts/login/', views.auth_login, name='auth_login'),
    path('accounts/logout/', views.auth_logout, name='auth_logout')
]