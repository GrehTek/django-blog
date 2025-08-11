from django.urls import path, include
from . import views

urlpatterns = [
    path('auth/login/', views.login_auth, name='login_auth'),
    path('auth/register/', views.register_auth, name='register_auth'),
]
