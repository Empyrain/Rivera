from .models import *
from time import strftime
from re import search

def delete_messages(message_text):
    '''Delete all messages from server. TODO: Turn off this function to all users without me'''
    if message_text == '::delete::':
        for i in Message.objects.all():
            i.delete()


def there_is_a_link(message_obj, start, end):
    import requests
    url = message_obj.text[start:end]
    if url[:3] == 'www':
        url = 'http://' + url
    print(url)
    try:
        response = requests.get(url)

    except:
        pass

def check_message(function):
    '''Decorator. Check a messages'''
    def wrapped(message_obj):
        succes_flag = True

        if message_obj.text == '::delete::':  #TODO: remove
            for i in Message.objects.all():
                i.delete()
                succes_flag = False

        while message_obj.text[0] == ' ':
            if len(message_obj.text) == 1:
                del message_obj
                succes_flag = False
            else: message_obj.text = message_obj.text[1:]

        while message_obj.text[-1] == ' ':
            message_obj.text = message_obj.text[:-1]

        url = '(http[s]?://|www.)(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
        regular_ex = search(url, message_obj.text)
        if regular_ex != None:
            there_is_a_link(message_obj, regular_ex.start(), regular_ex.end())

        if succes_flag != False:
            function(message_obj)

    return wrapped

@check_message
def save_message_from_form_to_db(message_obj):
    message_obj.save()

def get_message_from_form(request):
    """ Check message before save to db """

    if request.method == 'POST':
        try:
            data_from_form = MessageForm(request.POST)
            message_text = data_from_form['message']
            message_text = str(message_text)[74:-13]  #delete raw html tags

            message_obj = Message(
            text=message_text,
            date=strftime('%d/%m/%Y'),
            time=strftime('%H:%M:%S'),
            author=Users.objects.get(id=3) #now Incognito is 3
            )

            save_message_from_form_to_db(message_obj)

            del data_from_form
            del message_text
            del message_obj

        except: pass              #TODO!
    else: pass
