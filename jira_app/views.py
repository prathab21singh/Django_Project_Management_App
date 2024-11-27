from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
from django.http import HttpResponse
# from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . import AdminViews
from .models import CustomUser
from .authentication import EmailBackEnd

# Create your views here.
             
    
def loginPage(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # check admin login
        # valid_user = CustomUser.objects.filter(email=email)
        # print(valid_user,2222)
        # user = valid_user.authenticate(email=email, password=password)

        user = EmailBackEnd.authenticate(request, username=email, password=password)
        try:
            user.backend = 'django.contrib.auth.backends.ModelBackend'
        except:
            messages.error(request, "Invalid Login Credentials!")
            return redirect('login')

        if user!= None:
            login(request, user)
            user_type = user.user_data
            print(user_type,11111)
            if user.is_superuser:
                return redirect('admin_home')
            
            elif user_type == '2':
                return HttpResponse("<h1>Manager Page - Under Construction </h1>")
            
            elif user_type == '3':
                return HttpResponse("<h1>Employee Page - Under Construction </h1>")

            else:
                messages.error(request, "Invalid Login!")
                return redirect('login')
        else:
            messages.error(request, "Invalid Login Credentials!")
            return redirect('login')               
            

def signupPage(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    elif request.method == 'POST':
        #check password
        pwd1 = request.POST.get('pwd1')
        pwd2 = request.POST.get('pwd2')
        username = request.POST.get('username')
        email = request.POST.get('email')

        print(pwd1,pwd2)
        if not CustomUser.objects.filter(username=username).exists():
                if not CustomUser.objects.filter(email=email).exists():
                    if pwd1 == pwd2:
                        user = CustomUser.objects.create_superuser(
                            username=username,
                            email=email,
                            password=pwd1
                        )
                        user.save()
                        messages.success(request, 'Superuser created successfully!')
                        return redirect('login')
                    else:
                        messages.success(request, 'Password not matched!')
                        return redirect('signup')
                else:
                    messages.success(request, 'Email already exists!')
                    return redirect('signup')

        else:
            messages.success(request, 'Superuser already exists!')
            return redirect('signup')
        
def logout_user(request):
    logout(request)
    return redirect('login')