from django.contrib.auth.models import UserManager
from django.contrib.auth.hashers import make_password


class CustomUserManager(UserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            password=make_password(password),
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
            )
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        user = self._create_user(email, password, True, True, **extra_fields)
        return user
