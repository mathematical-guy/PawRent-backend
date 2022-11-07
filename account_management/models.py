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

    @property
    def is_pet_available(self):
        if self.user_type != UserConstants.UserType.OWNER:
            return False
        return False if self.owner_contracts.filter(is_active=True) else True


class Contract(models.Model):
    owner = models.ForeignKey(User, related_name="owner_contracts", on_delete=models.CASCADE)
    renter = models.ForeignKey(User, related_name="renter_contracts", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created At", null=True)
    duration = models.TimeField(verbose_name="Contract duration", null=True)
    is_active = models.BooleanField(default=False, verbose_name="Is Contract Active ?")

    def __str__(self):
        return f"{self.owner.username} - contract - {self.renter.username}"
