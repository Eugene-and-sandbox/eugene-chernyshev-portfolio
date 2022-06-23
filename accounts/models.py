from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, Group
)
from django.contrib.auth.models import PermissionsMixin


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    USER_ROLE = [
        ('CL', 'Client'),
        ('AD', 'Admin'),
    ]
    user_role = models.CharField(choices=USER_ROLE, max_length=2, default='CL')

    USER_POSITION = [
        ('MEN', 'Manager'),
        ('CEO', 'Chief Executive Officer'),
        ('FOU', 'Founder'),
        ('CLI', 'Client')
    ]
    user_position_1 = models.CharField(choices=USER_POSITION, max_length=3)
    user_position_2 = models.CharField(choices=USER_POSITION, max_length=3, blank=True)
    user_position_3 = models.CharField(choices=USER_POSITION, max_length=3, blank=True)
    name = models.CharField(max_length=30, blank=True)
    surname = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=150, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    picture = models.ImageField(upload_to='media/images/users/', blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

   

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.name} {self.surname}, {self.address}, {self.phone}, {self.email}'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


    