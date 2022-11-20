from pet.models import Pet
from rest_framework import serializers


class PetListAnonymousUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ("name", "age", "color", "category", "image")


class PetListAuthenticatedUserSerializer(PetListAnonymousUserSerializer):
    class Meta:
        model = Pet
        fields = ("name", "age", "color", "category", "image", "is_rented")
