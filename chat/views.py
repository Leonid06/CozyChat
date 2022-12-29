from django.shortcuts import render
from django.contrib.auth.models import User



def main(request): 
    # user = User.objects.create_user()
    return render(request, template_name= 'main.html')


def register(request):
    # if request.method == "POST" :
    #     form =
    return 

def login(request):
    return 
def logout(request): 
    return 
