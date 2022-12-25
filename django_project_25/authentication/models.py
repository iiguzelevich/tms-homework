from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    create_at = models.DateTimeField(auto_now_add=True)

    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username}'
