from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages 



def main(request): 
    context = {'username' : 'Anonym'}
    if request.user.is_authenticated:
        username = request.user.username 
        context['username'] = username 

    return render(request, template_name= 'main.html', context= context)


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        newUser = User.objects.create_user(username= username, password= password)
        newUser.save()
        login(request, newUser)
        return redirect('main')   
    return render(request, template_name= 'auth/register.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
    
        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            messages.error(request,'username or password not correct')
            return redirect('login_user')
    else:
         return render(request, template_name= 'auth/login.html')
   
def logout(request): 
    return 
