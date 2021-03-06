'''
underdev URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
'''
from django.contrib import admin
from django.urls import path
from personal.views import (
    HomeScreenView, 
)
from account.views import (
    registration_view,

)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeScreenView, name = "HOMEPAGE"),
    path('register/', registration_view, name = "register"),
]

#  <!-- {% include 'personal/snippets/body_snippet.html' with value=question %}<br>  I get error if I add extra white space in between the values assigned-->