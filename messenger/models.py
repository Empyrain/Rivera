from django.db import models
from django import forms

# Create your models here.

class Users(models.Model):
    ''' Group of users '''
    class Meta:
        db_table = "Users"
    name = models.CharField(max_length=20, blank=False, default="Incognito")
    status = models.BooleanField(default=0, blank=False) # offline / online
    permissions = models.IntegerField(default=2, blank=False)
    # settings = models.OneToOneField(Settings, primary_key=True)
    # avatar = models.ImegaField

class Message(models.Model):
    ''' Single message '''
    class Meta:
        db_table = "Message"
    message_id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=1000)                   #TODO
    time = models.CharField(max_length=8, blank=False, default='error')
    date = models.CharField(max_length=10, blank=False, default='error')
    author = models.ForeignKey(Users, on_delete=models.CASCADE)

class MessageForm(forms.Form):
    ''' Message form '''
    class Meta:
        db_table = "MessageForm"
    """ Get data from form. After move the data to Message object. """
    message = forms.CharField(max_length=1000)                                  #TODO

class Settings(models.Model):
    ''' User\'s settings '''
    class Meta:
        db_table = "Settings"
    sound_notifications = models.BooleanField()
    theme = models.CharField(default="light", max_length=5)
    font_size = models.IntegerField(default=17)
    two_step_verification = models.BooleanField(default=0)
    logout_time = models.IntegerField(default=20)
