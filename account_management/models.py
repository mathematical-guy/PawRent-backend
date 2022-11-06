from django.db import models
from django.contrib.auth.models import AbstractUser
from account_management.choices import USER_TYPES_CHOICES
from account_management.constants import UserConstants


class User(AbstractUser):
    user_type = models.CharField(
        max_length=32, choices=USER_TYPES_CHOICES, null=True, blank=True)
    contact_number = models.CharField(max_length=16)

    def __str__(self):
        return self.username


class Contract(models.Model):
    owner = models.ForeignKey(User, related_name="owner_contracts", on_delete=models.CASCADE)
    renter = models.ForeignKey(User, related_name="renter_contracts", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.owner.username} - contract - {self.renter.username}"
