from .models import Useraccount

def login_user(login, password):
    try:
        user = Useraccount.objects.get(email=login, password=password)
        return user
    except Useraccount.DoesNotExist:
        return None