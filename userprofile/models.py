from django.db import models

from django.db import models

class Useraccount(models.Model):
    email = models.CharField(primary_key=True, max_length=50)
    password = models.CharField(max_length=50)
    lastname = models.CharField(max_length=30)
    firstname = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=20, blank=True, null=True)
    phone_number = models.CharField(max_length=30, blank=True, null=True)
    photo = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'useraccount'