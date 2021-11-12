from django.urls import path
from . import views

urlpatterns = [
    # Register, Login, dashboard, logout
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('admin_dashboard', views.admin_dashboard, name='admin_dashboard'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout'),
]