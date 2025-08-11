from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/home', views.home, name='dashboard_home'),
    path('dashboard/logout_auth', views.logout_auth, name='logout_auth'),
]