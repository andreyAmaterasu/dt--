from django.shortcuts import render
from django.http import HttpResponse 
from .services import getUserWithEmail

def profile(request):
    if request.method == "POST":
        return HttpResponse("Задача создана")
    else:
        email = request.session.get('email')
        serialized_user = {"email": email}
        data_context = {"user_context": serialized_user}
        return render(request, "userprofile/profile.html", context=data_context)