from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from application.serializers import (
    UserSerializer,
    ClientSerializer,
    ContractSerializer,
    EventSerializer
    )
from application.models import User, Client, Contract, Event
from application.permissions import (
    UserPermission,
    ClientPermission,
    ContractPermission,
    EventPermission
    )


class UserViewset(ModelViewSet):
    permission_classes = [IsAuthenticated, UserPermission]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user_role = serializer.validated_data.get('role', '')
        if user_role == 'MANAGEMENT':
            is_staff = True
        else:
            is_staff = False
        serializer.save(is_staff=is_staff)


class ClientViewset(ModelViewSet):
    permission_classes = [IsAuthenticated, ClientPermission]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [SearchFilter]
    search_fields = ['first_name', 'last_name', 'email']

    def get_queryset(self):
        if self.request.user.role == 'SUPPORT':
            return self.queryset.filter(
                client_event__support_contact=self.request.user)
        elif self.request.user.role == 'SALES':
            return self.queryset.filter(sales_contact_id=self.request.user)
        return self.queryset


class ContractViewset(ModelViewSet):
    permission_classes = [IsAuthenticated, ContractPermission]
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    filter_backends = [SearchFilter]
    search_fields = [
        'client__first_name',
        'client__last_name',
        'client__email',
        'date_created',
        'amount'
        ]

    def perform_create(self, serializer):
        serializer.save(sales_contact=self.request.user)

    def get_queryset(self):
        if self.request.user.role == 'SALES':
            return self.queryset.filter(sales_contact=self.request.user)
        return self.queryset


class EventViewset(ModelViewSet):
    permission_classes = [IsAuthenticated, EventPermission]
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [SearchFilter]
    search_fields = [
        'client__first_name',
        'client__last_name',
        'client__email',
        'event_date'
        ]

    def get_queryset(self):
        if self.request.user.role == 'SUPPORT':
            return self.queryset.filter(support_contact=self.request.user)
        return self.queryset
