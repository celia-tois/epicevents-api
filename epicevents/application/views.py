from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from application.serializers import UserSerializer, ClientSerializer, ContractSerializer, EventSerializer
from application.models import User, Client, Contract, Event


class UserViewset(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ClientViewset(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ContractViewset(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer

    def perform_create(self, serializer):
        client_id = self.request.data.get('client')
        client = Client.objects.get(id=client_id)
        serializer.save(sales_contact=client.sales_contact)


class EventViewset(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Event.objects.all()
    serializer_class = EventSerializer
