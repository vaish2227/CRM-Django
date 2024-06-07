from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == 'POST':
        username1=request.POST['username']
        password1=request.POST['password']

        user= authenticate (request, username=username1,password=password1)
        if user is not None:
            login(request,user)
            messages.success(request,"Logged in successfully")
            return redirect('home')
        else:
            messages.success(request,"There was an error...Try again")
            return redirect('home') 
    else:
        return render(request,'home.html',{})


def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request,"Logged out")
    return redirect('home')

def register_user(request):
    return render(request,'register.html',{})
