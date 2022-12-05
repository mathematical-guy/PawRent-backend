from pet.models import Pet
from rest_framework import serializers
from rest_framework import generics


class PetListAnonymousUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ("name", "age", "color", "category", "image")


class PetListAuthenticatedUserSerializer(PetListAnonymousUserSerializer):
    verbose_category = serializers.SerializerMethodField()

    class Meta:
        model = Pet
        fields = ("id", "name", "age", "category", "verbose_category", "image", "is_rented")

    def get_verbose_category(self, pet: Pet):
        return pet.category.get_category_display()


class PetDetailSerializer(PetListAuthenticatedUserSerializer):
    class Meta:
        model = Pet
        fields = (
            "id", "name", "age", "color", "category", "verbose_category", "image", "is_rented",
            "owner_name", "owner_contact",
        )
