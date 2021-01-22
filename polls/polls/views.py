from django.shortcuts import HttpResponse

# Create your views here.
# Sample code here
def index(request):
    return HttpResponse("Hello, World. You're at the polls index")
