from rest_framework.serializers import ModelSerializer
from application.models import User, Client, Contract, Event
from django.contrib.auth.hashers import make_password


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'role', 'password')

    def validate_password(self, value: str) -> str:
        """
        Hash value passed by user.
        :param value: password of a user
        :return: a hashed version of the password
        """
        return make_password(value)


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class ContractSerializer(ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'
        read_only_fields = ('sales_contact', )


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        