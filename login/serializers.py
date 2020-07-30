from rest_framework.serializers import ModelSerializer
from .models import Useraccount
from rest_framework import serializers

class UseraccountSerializer(ModelSerializer):
    class Meta:
        model = Useraccount
        fields = "__all__"
    