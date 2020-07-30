from rest_framework.routers import DefaultRouter
from django.urls import path
from . import views

router = DefaultRouter()
router.register("useraccount", views.UseraccountViewSet)

urlpatterns = [
    path('registration', views.registration, name='registration'),
    path('', views.login),
]

urlpatterns += router.urls