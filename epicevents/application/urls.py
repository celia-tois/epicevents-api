from django.urls import path
from application.views import UserViewset


urlpatterns = [
    path('users/', UserViewset.as_view()),
]