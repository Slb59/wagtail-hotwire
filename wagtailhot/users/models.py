from django.contrib.auth import models as auth_models
from django.db import models
from django.utils.translation import gettext_lazy as _

class WagUser(auth_models.AbstractUser):
    first_name = None
    last_name = None
    username = None
    email = models.EmailField(_("email address"), unique=True, max_length=50)
    trigram = models.CharField(max_length=5, blank=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["trigram"]

    def __str__(self):
        return f"{self.trigram}"
    
    class Meta:
        verbose_name_plural = "users"
        verbose_name = "user"
        ordering = ["-trigram"]
        indexes = [
            models.Index(fields=["-trigram"]),
        ]


class Profil(models.Model):
    user = models.OneToOneField(WagUser, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="photos/", blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "users profil"

    def __str__(self) -> str:
        return self.user.username
