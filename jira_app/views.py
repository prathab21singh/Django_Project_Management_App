from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

# Create your views here.

def loginPage(request):
    return render(request, 'login.html')

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
        if not User.objects.filter(username=username).exists():
                if not User.objects.filter(email=email).exists():
                    if pwd1 == pwd2:
                        user = User.objects.create_superuser(
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