from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='bloghome'),
    path('blogpost/edit/<int:pk>/', views.edit_blogpost, name='edit_blogpost'),
    path('blogpost/delete-post/<int:pk>', views.delete_blogpost, name='delete_blogpost'),
    path('blogpost/blog-comment/<int:pk>/', views.blog_comment, name='blog_comment'),

    path('blogpost/send-data/', views.receive_data, name='send_data'),
]
