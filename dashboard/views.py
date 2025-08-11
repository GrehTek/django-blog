from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import decorators,logout
from blog.forms import BlogPostForm
from django.contrib import messages

# Create your views here.

@login_required
def home(request):

  if request.method == 'POST':
    post = BlogPostForm(request.POST)

    if post.is_valid():
      post.save()
      messages.success(request, "Post Added")
      return redirect("bloghome")


  return render(request, 'home.html')

@login_required
def logout_auth(request):

  if request.method == 'POST':
    logout(request)
    return redirect('bloghome')
  
  return render(request, 'logout.html')