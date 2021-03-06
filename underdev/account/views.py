from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

from account.forms import RegistrationForm

# Create your views here.

def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email = email, password = raw_password)
            login(request, account)
            return redirect('home')

        else:
            context['registration_form'] = form
    else: # this will a GET request
        form = RegistrationForm()
        context['registration_form'] = form

    return render(request, 'accounts/register.html/', context)

# defining the logout in the site
def logout_view(request):
    logout(request)
    return redirect('home')

    
