from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, AbstractUser
from . import manager

from django.utils.translation import gettext_lazy as _

# Create your models here.


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True, blank=True, null=True)
    number = models.CharField(max_length=50, unique=True)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = "number"
    REQUIRED_FIELDS = ["username"]

    objects = manager.UserManager()

    def __str__(self) -> str:
        return self.username

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def has_perm(self, perm, obj=None) -> bool:
        return self.is_admin

    def has_module_perms(self, app_label: str) -> bool:
        return True
