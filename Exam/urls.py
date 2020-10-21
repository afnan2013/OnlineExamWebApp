from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', LoginView.as_view(), name="login_url"),
    path('register/', views.register, name='register_url'),
    path('logout/', LogoutView.as_view(next_page='login_url'), name="logout"),
    path('result', views.result, name='result'),
    path('questions/<str:choice>', views.questions, name='questions'),
]
