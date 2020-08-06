from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthdate = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'Профиль пользователя {self.user.username}'
