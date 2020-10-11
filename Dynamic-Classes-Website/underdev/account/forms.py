from django import forms
from django.contrib.auth.forms import UserCreationForm
import underdev.settings.configure()

from account.models import Account

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length = 60, help_text = 'Required, Add a valid email address') # This is will be shown adjacent to field

    class Meta:
        model = Account
        fields = {"email", "username", "password1", "password2"}
        


