from django.shortcuts import render
from django.http import HttpResponse

from .models import *
from .message_logic import *

# Create your views here.

def get_messages_from_db():
    '''  Get list of Message objects from database and return the dict '''
    return {'messages': Message.objects.all()}

def index(request):
    ''' Render main page. TODO: organizer.mephi.prj sm'''
    get_message_from_form(request)
    context = get_messages_from_db()
    return render(request, 'messenger/main.html', context)

def page_not_found(request):
    ''' Return #404 template'''
    context = {}
    return render(request, '404/404.html', context)
