from django.urls import path
from . import views

#uRLConf
urlpatterns = [
    path('',views.Index, name='index'),
    path('signup/',views.SignUp, name='signup'),
    path('login/',views.Login, name='login'),
    # user
    path('home/',views.Home, name='home'),
    path('fullmenu/',views.FullMenu, name='fullmenu'),
    path('reviews/',views.Review, name='review'),
    path('logout/',views.HandleLogout, name='logout'),
    path('viewFood/<int:id1>',views.viewFood, name='viewFood'),
    path('updatecart/<int:id2>',views.updatecart, name='updatecart')

]