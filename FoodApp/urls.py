from django.urls import path
from . import views

#uRLConf
urlpatterns = [
    path('signup/',views.SignUp, name='signup'),
    path('login/',views.Login, name='login'),
    path('home/',views.Home, name='home'),
    path('logout/',views.HandleLogout, name='logout')
]