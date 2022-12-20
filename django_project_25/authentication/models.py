from datetime import datetime
from datetime import timedelta

import jwt
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from config import settings


class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None):

        if not username:
            raise TypeError('users must have "username"')

        if not email:
            raise TypeError('users must have "email address"')

        user = self.model(
            username=username,
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):

        if not username:
            raise TypeError('superusers must have "username"')

        if not email:
            raise TypeError('superusers must have "email address"')

        if not password:
            raise TypeError('superusers must have "password"')

        user = self.create_user(
            username=username,
            email=email,
            password=password
        )

        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    username = models.CharField(
        db_index=True,
        max_length=255,
        unique=True
    )

    email = models.EmailField(
        db_index=True,
        unique=True,
    )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    def __str__(self):
        return f'{self.username} {self.email}'

    def _generate_jwt_token(self):
        dt = datetime.now() + timedelta(days=1)

        payload = {
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }

        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

        return token

    @property
    def token(self):
        return self._generate_jwt_token()

    def get_full_name(self):
        return self.username
