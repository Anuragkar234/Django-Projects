from django import forms
from .models import TODO

class CreateForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'Placeholder':'Add your task here'}))

    class Meta:
        model: TODO
        fields = '__all__'