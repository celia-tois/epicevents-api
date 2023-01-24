from rest_framework import routers
from django.urls import path, include
from application.views import UserViewset, ClientViewset, ContractViewset, EventViewset


router = routers.SimpleRouter()
router.register(r'users', UserViewset)
router.register(r'clients', ClientViewset)
router.register(r'contracts', ContractViewset)
router.register(r'events', EventViewset)


urlpatterns = [
    path('', include(router.urls))
]
