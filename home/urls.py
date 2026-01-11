from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('course/<slug:slug>/', views.course_detail, name='course_detail'),
    path('course/<slug:slug>/daftar/', views.course_register, name='course_register'),
    path('course/<slug:slug>/konfirmasi/', views.course_confirm, name='course_confirm'),
    path('course/<slug:slug>/pay/', views.process_payment, name='process_payment'),
    path('course/<slug:slug>/success/', views.payment_success, name='payment_success'),
    path('about/', views.about, name='about'),
]
