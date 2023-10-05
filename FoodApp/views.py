from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import FoodItem,Category,tbl_rating
from . import naive as s


# Create your views here.


cart_quantity=dict()
cart_price = dict()
cart_name = dict()
count = 0

def updatecount():
    global cart_dict
    global count
    count = count+1


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

@login_required(login_url='login')
def WriteReview(request, id3):

    postivecount=0
    negativecount=0
    allremarks = tbl_rating.objects.all()
    total=len(allremarks)
    for r in allremarks:
        if r.sentiment == 'positive':
            postivecount=postivecount+1
        if r.sentiment=="negative":
            negativecount==negativecount+1     


    if request.method == "POST":
        remarks = request.POST.get('remarks')
        cumstomer_id = request.user.id
        menu_id = FoodItem.objects.get(id=id3).id
        newreview = tbl_rating(remarks=remarks, customer_name_id=cumstomer_id, menu_id=menu_id,sentiment=s.prediction(remarks))
        newreview.save()
        # messages.success(request,"review added")
        # return redirect('writereviews.html')
    allremarks = tbl_rating.objects.all()
    

    food=FoodItem.objects.filter(id=id3)
    placeholder=1
    for obj in food:
        idproduct=obj.id
        c =obj.category
    rfood = FoodItem.objects.filter(category=c)
    if idproduct in cart_quantity.keys():
        placeholder=cart_quantity[idproduct]
    return render(request,'writereviews.html',{"reviews": allremarks, "foods":food,"productsquantity":cart_quantity,"placeholder":placeholder,"rfoods":rfood,"title":"viewfood"})



# add to cart code
def updatecart(request, id2):
    global cart_price
    global cart_name
    global cart_quantity
    global count
    updatecount()
    quantity = request.POST.get('quantity','1')
    cart_quantity[id2]=quantity
    p=FoodItem.objects.filter(id=id2)
    for obj in p:
        price=obj.price
        name=obj.name
        cart_name[id2]=name
        cart_price[id2]=price
    messages.success(request,"Item added to cart")
    return redirect('/viewfood/'+str(id2))

def Index(request):
    return render(request, 'index.html')

def viewFood(request,id1):
    food=FoodItem.objects.filter(id=id1)
    placeholder=1
    for obj in food:
        idproduct=obj.id
        c =obj.category
    rfood = FoodItem.objects.filter(category=c)
    if idproduct in cart_quantity.keys():
        placeholder=cart_quantity[idproduct]
    return render(request,'viewfood.html',{"foods":food,"productsquantity":cart_quantity,"placeholder":placeholder,"rfoods":rfood,"title":"viewfood"})
    # return render(request, 'viewFood.html')     

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
        user=authenticate(request,username=username,password=password)
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



