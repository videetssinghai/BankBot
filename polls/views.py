from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from .forms import *
from django.views.generic import CreateView
from django.views.generic import View
from django.template import loader
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User


    # Create your views here.

def chatApp(request):
    template=loader.get_template("chat.html")
    return HttpResponse(template.render())

def chatbotResponse(request):
     var = request.GET.get('sentence')
     print str(var)
     response_data ={ 'key': str(var)
          }
     return JsonResponse(response_data)

class Registration(View):
        form_class = UserForm

        def get(self, request):
            form = UserForm()
            return render(request, 'signup.html', {'form': form})

        def post(self, request):
            form = self.form_class(request.POST)

            if form.is_valid():
               User.objects.create_user(request.POST['Email'],request.POST['Email'],request.POST['Password'])
               template = loader.get_template("chat.html")
               return HttpResponse(template.render())


class login_page(CreateView):
    form_class = LoginForm

    def get(self, request):
        form = LoginForm()
        print form
        return render(request, 'login.html',{'form': form})

    def post(self, request):

        Email = request.POST['Email']
        Password = request.POST['Password']
        print Email + '    ' + Password
        user = authenticate(username=Email,password=Password)

        if user is not None:
            login(request,user)
            # Redirect to a success page.
            return HttpResponseRedirect('/chat/Home')


        else:
            return HttpResponse("not authenticated")

def Home(self):
    template = loader.get_template("chat.html")
    return HttpResponse(template.render())


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/chat/login')



