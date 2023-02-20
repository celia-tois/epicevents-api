from rest_framework.permissions import BasePermission
from application.models import Client

class UserPermission(BasePermission):
    """
    Allow only users in the Management team to perform a POST, GET, PUT and DELETE.
    """
    def has_permission(self, request, view):
        user_role = request.user.role
        if user_role == 'MANAGEMENT':
            return True
        return False


class ClientPermission(BasePermission):
    def has_permission(self, request, view):
        """
        Allow users in the Management team and the Support team to perform a GET.
        Allow users in the Sales team to perform a GET and a POST.
        """
        user_role = request.user.role
        if user_role == 'MANAGEMENT' and request.method in ['GET', 'PUT']:
            return True
        if user_role == 'SUPPORT' and request.method == 'GET':
            return True
        if user_role == 'SALES':
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        """
        Allow users in the Management team to perform a GET and a PUT for every client.
        Allow users in the Support team to perform a GET if the client is assigned to them.
        Allow users in the Sales team to perform a GET and a PUT if the client is assigned to them.
        """
        user_role = request.user.role
        if user_role == 'MANAGEMENT' and request.method in ['GET', 'PUT']:
            return True
        if user_role == 'SUPPORT' and request.method == 'GET':
            if obj in Client.objects.filter(id=obj.id, client_event__support_contact=request.user):
                return True
        if user_role == 'SALES' and request.method in ['GET', 'PUT']:
            if obj in Client.objects.filter(id=obj.id, sales_contact_id=request.user):
                return True
        return False


class ContractPermission(BasePermission):
    def has_permission(self, request, view):
        """
        Allow users in the Management team to perform a GET.
        Allow users in the Sales team to perform a GET and a POST.
        """
        user_role = request.user.role
        if user_role == 'MANAGEMENT' and request.method in ['GET', 'PUT']:
            return True
        if user_role == 'SALES':
            return True
        return False

    def has_object_permission(self, request, view, obj):
        """
        Allow users in the Management team to perform a GET and a PUT for every client.
        Allow users in the Sales team to perform a GET and a PUT if the contract is assigned to them.
        """
        user_role = request.user.role
        if user_role == 'MANAGEMENT' and request.method in ['GET', 'PUT']:
            return True
        if user_role == 'SALES' and obj.sales_contact == request.user and request.method in ['GET', 'PUT']:
            return True
        return False

    
class EventPermission(BasePermission):
    def has_permission(self, request, view):
        """
        Allow users in the Management team to perform a GET.
        Allow users in the Support team to perform a GET.
        Allow users in the Sales team to perform a GET and a POST.
        """
        user_role = request.user.role
        if user_role == 'MANAGEMENT' and request.method in ['GET', 'PUT']:
            return True
        if user_role == 'SUPPORT' and request.method in ['GET', 'PUT']:
            return True
        if user_role == 'SALES' and request.method == 'POST':
            return True
        return False

    def has_object_permission(self, request, view, obj):
        """
        Allow users in the Management team to perform a GET and a PUT for every client.
        Allow users in the Support team to perform a GET and a PUT if the event is assigned to them.
        """
        user_role = request.user.role
        if user_role == 'MANAGEMENT' and request.method in ['GET', 'PUT']:
            return True
        if user_role == 'SUPPORT' and obj.support_contact == request.user:
            if request.method == 'GET':
                return True
            if request.method == 'PUT' and obj.event_status != 'FINISHED':
                return True
        return False
