from django.db import models
from pet.constants import PetConstants, PetCategoryConstants, PetOwnerConstants
from pet.choices import PET_CATEGORY_CHOICES


class PetCategory(models.Model):
    category = models.CharField(
        max_length=PetCategoryConstants.ModelConstants.CATEGORY_MAX_LENGTH, verbose_name="Category Type",
        choices=PET_CATEGORY_CHOICES,
    )

    # Add tags or some other functionality

    class Meta:
        verbose_name_plural = "Pet Categories"


class Pet(models.Model):
    name = models.CharField(
        max_length=PetConstants.PET_NAME_MAX_LENGTH, verbose_name="Pet Name")
    age = models.PositiveIntegerField(verbose_name="Pet Age")
    color = models.CharField(
        max_length=PetConstants.PET_COLOR_MAX_LENGTH, verbose_name="Pet Color", null=True)
    owner_name = models.CharField(
        max_length=PetOwnerConstants.OWNER_NAME_MAX_LENGTH, verbose_name="Owner Name")
    owner_contact = models.CharField(
        max_length=PetOwnerConstants.OWNER_CONTACT_MAX_LENGTH, verbose_name="Owner Contact Number")

    category = models.ForeignKey(
        PetCategory, related_name="pets", verbose_name="Pet Category", on_delete=models.SET_NULL,
        null=True)
    image = models.ImageField(null=True, verbose_name="Pet Photo", upload_to="pets-profile/")
    is_rented = models.BooleanField(default=False, verbose_name="Is Pet Rented ?")

    def __str__(self):
        return f"{self.name} - {self.category.name}"
