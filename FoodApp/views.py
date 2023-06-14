from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages

# Create your views here.
def SignUp(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')


        # print(name,email,phone,pass1,pass2)

        if pass1==pass2:
            new_user=User.objects.create_user(name,email,pass1,first_name=name)
            user=authenticate(username=name,password=pass1)
            return HttpResponse('user created successfullyy!!!!')
            # if user is not None:
            #     login(request,user)
            #     return redirect('foryou')
        
        else:
            messages.error(request,"wrong passwords combination")
            return HttpResponse("error 404")



    return render(request, 'singup.html')
    # return HttpResponse('hey')

def Login(request):
    return render(request, 'login.html')
    # return HttpResponse('hey')

def Home(request):
    return render(request, 'home.html')    
