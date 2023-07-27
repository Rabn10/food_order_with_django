from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import FoodItem,Category

# Create your views here.



@login_required(login_url='login')
def Home(request):
    return render(request, 'home.html')
 
@login_required(login_url='login')
def FullMenu(request):
    foods=FoodItem.objects.all()
    categorys=Category.objects.all()
    for x  in foods:
        print(x.name)
    return render(request, 'fullmenu.html',{"foods":foods,"categories":categorys,"title":"Fullmenu"})

@login_required(login_url='login')
def Review(request):
    return render(request, 'reviews.html')

def Index(request):
    return render(request, 'index.html')

def viewFood(request) :
    return render(request, 'viewFood.html')     

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
            # return HttpResponse('user created successfullyy!!!!')
            if user is not None:
                login(request,user)
                return redirect('login')
        
        else:
            messages.error(request,"wrong passwords combination")
            return HttpResponse("error 404")



    return render(request, 'singup.html')
    # return HttpResponse('hey')

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"invalid credentials")
            return redirect('login')
        
    return render(request, 'login.html')
    # return HttpResponse('hey')



def HandleLogout(request):
    logout(request)
    return redirect('login')
    # return render(request, 'logout.html')  
