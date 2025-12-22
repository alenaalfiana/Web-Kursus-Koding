from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('kursus/<str:slug>/', views.detail, name='detail'),
    path('kursus/<str:slug>/daftar/', views.daftar, name='daftar'),
    path('sukses/', views.sukses, name='sukses'),
]