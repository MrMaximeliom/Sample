from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.db import models
from django.utils.translation import gettext_lazy as _

class UserAccountManager(BaseUserManager):

    def create_user(self, full_name, phone_number, password=None, **extra_fields):

        if not full_name:
            raise ValueError(_('Users must provide their full name'))
        if not phone_number:
            raise ValueError(_('Users must provide their phone number'))

        # phone_number.setdefault('is_staff', True)
        user = self.model(
            full_name=full_name,
            phone_number=phone_number,

        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, full_name, phone_number,
                         password):
        user = self.create_user(
            full_name=full_name,
            phone_number=phone_number,
            password=password

        )
        user.admin = True
        user.staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    full_name = models.CharField(
        verbose_name=_('Full Name'),
        max_length=350,
        blank=False,
        null=False
    )
    phone_number = models.CharField(
        verbose_name=_('Phone Number'),
        blank=False,
        null=False,
        max_length=100,
        unique=True
    )

    email = models.EmailField(
        verbose_name=_('Email Address'),
        max_length=255,
        unique=True,
        blank=True,
        null=True
    )

    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now=True, blank=True, null=True)
    registration_datetime = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password', 'full_name','phone_number']
    objects = UserAccountManager()

    def get_full_name(self):
        # The user is identified by their email address
        return self.full_name

    def __str__(self):
        return self.full_name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # return self.user_role == 3
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        # return self.user_role == 1
        return self.admin



