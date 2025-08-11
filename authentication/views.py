from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
import random
import string
from django.http import HttpResponse

# Create your views here.
def generate_random(last_name):

  number = random.randint(0,9999)
  letters = ''.join(random.choices(string.ascii_uppercase, k=2))

  return f"{last_name}{number}{letters}"

def login_auth(request):

  User = get_user_model()
  
  if request.method == 'POST':
    email = request.POST.get('email')
    password = request.POST.get('password')

    # ensure fields are not empty
    if not email or not password:
      messages.error(request, "Email and Password are required")
      return redirect('login_auth')

    # authenticate
    try:
      user = User.objects.get(email=email)
    except User.DoesNotExist:
      messages.error(request, "User does not exist")
      return redirect('login_auth')

    if not user.check_password(password):
      messages.error(request, "Incorrect Password")
      return redirect('login_auth')

    if not user.is_active:
      messages.error(request, "User is not active")
      return redirect('login_auth')

    # login user
    login(request, user)
    return redirect('dashboard_home')

  return render(request, 'login.html')

def register_auth(request):
  
  if request.method == 'POST':
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    password = request.POST.get('password')
    confirm_password = request.POST.get('confirm-password')

    # ensure form field not empty
    if not first_name and last_name and email and password and confirm_password:
      messages.error(request, "All fields are required")
      redirect("register_auth")
    else:
      pass


    # validate pass and conf pass
    if password != confirm_password:
      messages.warning(request, "Password Mismatch")
      redirect('register_auth')

    # ensure not user already exist with same email address
    if User.objects.filter(email=email).exists():
      messages.error(request, "Email already exist")
      return redirect('register_auth')
    else:
      user = User.objects.create(
        first_name=first_name, 
        last_name=last_name, 
        email=email, 
        username=generate_random(last_name),
        password=make_password(password),
      )
      messages.success(request, "Registration Successful, Login")
      return redirect('login_auth')
      
     

  return render(request, 'register.html', {})

