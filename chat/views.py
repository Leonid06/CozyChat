from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages 



def main(request): 
    # user = User.objects.create_user()
    return render(request, template_name= 'main.html')


def register(request):
    # if request.method == "POST" :
    #     form =
    return 

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
    
        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            return redirect('main')
    else:
         return render(request, template_name= 'auth/login.html')
   
def logout(request): 
    return 
