from django.shortcuts import render
from django.http import HttpResponse
# from django.template.loader import render_to_string

from .models import *
from time import strftime

# Create your views here.

def save_message_from_form(request):
    """ Get message from form and save to db """

    if request.method == "POST":
        try:
            data_from_form = MessageForm(request.POST)
            message_text = data_from_form['message']
            message_text = str(message_text)[74:-4]     #delete raw html tags

            message_obj = Message(
            text=message_text,
            date=strftime('%d/%m/%Y'),
            time=strftime('%H:%M:%S'),
            # Users.objects.get(id=1) -> "incognito". TODO: After should be
            # replaced by current User (e.g. from auth field)
            author=Users.objects.get(id=1)
            )

            if message_obj.check_message() == True:
                message_obj.save()
                delete_messages(message_text)         #TODO DELETE !!!!
                del message_obj
                del data_from_form
                del message_text
        except:                                       #TODO!
            pass
    else:
        pass

def delete_messages(message_text):         #TODO DELETE !!!!
    if message_text == '::delete::':
        for i in Message.objects.all():
            print(i.text)
            i.delete()


def get_messages_from_db():
    """  Get list of Message objects from database and return the dict """
    return {'messages': Message.objects.all()}


def index(request):
    """ Render main page. TODO: organizer.mephi.prj sm"""

    save_message_from_form(request)
    context = get_messages_from_db()
    return render(request, 'messenger/main.html', context)

def page_not_found(request):
    """ Return #404 template"""
    context = {}
    return render(request, '404/404.html', context)

    #
    # response = render_to_response(
    # '404/404.html',
    # context_instance=RequestContext(request)
    # )
    # response.status_code = 404
    # return response
