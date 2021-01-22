from django.shortcuts import render
from account.models import Account
#from personal.models import Question

# Create your views here.
def HomeScreenView(request):

    # Context implemented in two ways as fiven below
    context = {}
    
    #context = {}
    #context['some_string'] = "this is some string I am passing to the view"
    #context['some_number'] = 864196

    #context = {
    #    'some_string' : "this is some string I am passing to the view",
    #    'some_string' : "this is some string I am passing to the view",
    #} 

    #list_of_values = []
    #list_of_values.append("first entry")
    #list_of_values.append("second entry")
    #list_of_values.append("third entry")
    #list_of_values.append("forth entry")

    #context['list_of_values'] = list_of_values

    accounts = Account.objects.all()
    context['accounts'] = accounts

    # now quering the data obtained
    #questions = Question.objects.all()
    #context['question'] = questions 


    return render (request, "personal/home.html", context) #The brackets are the context

# In django will be using snippets if we are using Veiws again and again
# Built in user model main issue is that it uses username as the entry point which is not neccessary be the case every time """