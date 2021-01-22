# this is the form representation of the model

from django import forms
from django.forms import  ModelForm

from .models import *

class TaskForm(forms.ModelForm):

    class Meta:
        # here we need a minimum a 2 values
        model = Task 
        fields = '__all__'
        