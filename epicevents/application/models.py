from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import AbstractBaseUser
from decimal import Decimal
from .managers import CustomUserManager


class User(AbstractBaseUser):
    ROLE_CHOICES = [
        ('MANAGEMENT', 'Management'),
        ('SALES', 'Sales'),
        ('SUPPORT', 'Support'),
    ]

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(db_index=True, unique=True, max_length=250)
    role = models.CharField(choices=ROLE_CHOICES, max_length=20)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'role']

    objects = CustomUserManager()

    def has_module_perms(self, app_label):
        return self.is_staff

    def has_perm(self, perm, obj=None):
        return self.is_staff


class Client(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(db_index=True, unique=True, max_length=100)
    phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    company_name = models.CharField(max_length=250)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    sales_contact = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        limit_choices_to={'role': 'SALES'}
        )


class Contract(models.Model):
    sales_contact = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        limit_choices_to={'role': 'SALES'}
        )
    client = models.ForeignKey(
        Client,
        on_delete=models.PROTECT,
        related_name="client_contract"
        )
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_signed = models.BooleanField()
    amount = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))]
        )
    payment_due = models.DateTimeField()


class Event(models.Model):
    STATUS_CHOICES = [
        ('CREATED', 'Created'),
        ('FINISHED', 'Finished'),
    ]

    client = models.ForeignKey(
        Client,
        on_delete=models.PROTECT,
        limit_choices_to={'client_contract__is_signed': True},
        related_name="client_event",
        )
    contract = models.ForeignKey(
        Contract,
        on_delete=models.PROTECT,
        limit_choices_to={'is_signed': True},
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    support_contact = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        limit_choices_to={'role': 'SUPPORT'}
        )
    event_status = models.CharField(choices=STATUS_CHOICES, max_length=20)
    attendees = models.IntegerField(validators=[MinValueValidator(1)])
    event_date = models.DateTimeField()
    notes = models.CharField(max_length=300)
