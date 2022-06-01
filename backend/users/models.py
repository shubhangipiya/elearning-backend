from django.db import models

# Create your models here.
from email.policy import default
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

from backend import settings

USER_TYPES = (
    ('user', 'User'),
    ('admin', 'Admin'),
)

User = settings.AUTH_USER_MODEL


class CustomAccountManager(BaseUserManager):
    def create_superuser(self, email, user_name, password, **other_fields):

        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_staff', True)

        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, password, **other_fields)

    # remove phone_number when creating new super user
    def create_user(self, email, user_name, password, phone_number, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          phone_number=phone_number, **other_fields)
        user.set_password(password)
        user.save()
        return user


class NewUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    phone_number = models.CharField(
        max_length=30, blank=False, default="0000000000")

    is_staff = models.BooleanField(default=False)
    user_type = models.CharField(
        choices=USER_TYPES, max_length=100, default="user")

    # This true signifies that the user can now use login function
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()

    # This email is used for the username field field while login
    USERNAME_FIELD = 'email'
    # Required fields that must be filled to submit the form
    REQUIRED_FIELDS = ['user_name']

    def __str__(self):
        return self.email
