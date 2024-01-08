from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('loginpage',views.loginpage,name='loginpage'),
    path('signup',views.signup,name='signup'),
    path('about',views.about,name='about'),
    path('usercreate',views.usercreate,name='usercreate'),
    path('login1',views.login1,name='login1'),
    path('logout',views.logout,name='logout'),
    path('adminpage',views.adminpage,name='adminpage'),
    
]