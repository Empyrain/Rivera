from django.shortcuts import render
from messenger.models import Users
from .models import *

# Create your views here.

def index(request):
    context = {}
    return check_login_data(request, context)

def check_login_data(request, context):
    if request.method == "POST":
        flag = False
        for user in Users.objects.all():
            if request.POST['login'] == user.name:
                flag = True
                print('Hello, {}'.format(user.name))
                user.status = 1 #online. Do not foget get offline with logout
                context['name'] = request.POST['login']
                context['WhoAmI'] = user
                print(context['WhoAmI'])
                return render(request, 'messenger/main.html', context)
            else:
                if flag == False:
                    context['error'] = 'Wrong login'
                    return render(request, "login/login_page.html", context)
    elif request.method == "GET":
        return render(request, "login/login_page.html", context)
    else: return render(request, "login/login_page.html", context)
