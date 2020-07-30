from .models import Useraccount

def getUserWithEmail(email):
    return Useraccount.objects.get(email=email)