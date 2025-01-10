from django.contrib.auth.models import User
from django.db import models


class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="photos/", blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "users profil"

    def __str__(self) -> str:
        return self.user.username
