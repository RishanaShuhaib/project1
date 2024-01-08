from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
    return render(request,'index.html')
def loginpage(request):
    return render(request,'login.html')
def signup(request):
    return render(request,'signup.html')
#@login_required(login_url='login')
def about(request):
    #if request.user.is_authenticated:
        
    #if 'uid' in request.session:
        return render(request,'about.html')
    #else:
       #return render(request,'login.html')
def usercreate(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        user_name = request.POST['username']
        emails = request.POST['email']
        pass_word = request.POST['password']
        cpass_word = request.POST['cpassword']
        
        if pass_word == cpass_word:
            if User.objects.filter(username=user_name).exists():  # check if username already exists
                messages.info(request, 'This username already exists!!!!')
                return redirect('signup')
            else:
                user = User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=user_name,
                    email=emails,
                    password=pass_word)
                user.save()
                messages.info(request, 'User created successfully')
                
               
        else:
            messages.info(request, 'Password does not match')
            return redirect('signup')

       # return redirect('login')

    return render(request, 'signup.html')

def login1(request):
    if request.method=='POST':
        user_name=request.POST['username']
        pass_word=request.POST['password']
        user=auth.authenticate(username=user_name,password=pass_word)
        if user is not None:
            #request.session['uid']=user.id
            if  user.is_staff:
                login(request,user)
                return redirect('adminpage')
            else:
                login(request,user)
                auth.login(request,user)
                messages.info(request,f'welcome {user_name}')
                return render(request,'about.html')
        else:
            messages.info(request,'invalid username or password')
            return redirect('/')
    return render(request,'index.html')
            
                
            #auth.login(request,user)
            #messages.info(request,f'Welcome {user_name}')
            #return redirect('about')
        #else:
            #messages.info(request,'Invalid Username or Password.Try Again.')
            #return redirect('login')
    #else:
        #return redirect('login')
#@login_required(login_url='login')
def logout(request):
    #request.session['uid']=''
    #if request.user.is_authenticated:
        
    auth.logout(request)
    return redirect('index')
def adminpage(request):
    return render(request,'adminlogin.html')
        