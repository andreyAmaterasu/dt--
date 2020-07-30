from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import UserForm
from . import services
from rest_framework.viewsets import ModelViewSet
from .serializers import UseraccountSerializer
from .models import Useraccount

class UseraccountViewSet(ModelViewSet):
    serializer_class = UseraccountSerializer
    queryset = Useraccount.objects.all()

def login(request):
    if request.method == "POST":
        entered_email= request.POST.get("login")
        entered_password = request.POST.get("password")
        user = services.login_user(entered_email, entered_password)

        if user is not None:
            request.session['email'] = entered_email
            return HttpResponseRedirect("/profile")
        else:
            userform = UserForm()
            return render(request, "login/login.html", {"form": userform, "error": True})
    else:
        userform = UserForm()
        return render(request, "login/login.html", {"form": userform})

def registration(request):
    if request.method == "GET":
        return render(request, "login/registration.html")
