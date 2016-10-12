from django.shortcuts import render
from messenger.models import Users
from .models import *
from messenger.models import Message

# Create your views here.

def index(request):
    context = {}
    return check_login_data(request, context)

def check_login_data(request, context):
    ''' Check auth data '''
    if 'login' in request.POST:
        for user in Users.objects.all():
            if request.POST['login'] == user.name:
                user.status = 1 #online. Do not foget get offline with logout
                context['name'] = request.POST['login']
                context['messages'] = Message.objects.all()
                return render(request, 'messenger/main.html', context)
        else:
            context['error'] = 'Wrong login'
            return render(request, "login/login_page.html", context)
    else:
        context = {}
        return render(request, "login/login_page.html", context)
