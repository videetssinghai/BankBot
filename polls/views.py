from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.http import JsonResponse
from .forms import UserForm

from django.template import loader
# Create your views here.
def chatApp(request):
    template=loader.get_template("chat.html")
    return HttpResponse(template.render())

def chatbotResponse(request):
    var = request.GET.get('sentence')
    print str(var)
    response_data ={
        'key': str(var)
    }
    return JsonResponse(response_data)

def signup(request):
    form = UserForm()
    return render(request, 'signup.html', {'form':form})




