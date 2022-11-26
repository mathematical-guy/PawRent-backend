from rest_framework import serializers
from pet.models import Pet, PetCategory




class PetSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        queryset=PetCategory.objects.all(), slug_field="category",
        error_messages={"does_not_exist": 'Pet Category {value} does not exist.'}
    )

    class Meta:
        model = Pet
        fields = (
            "id", "name", "age", "color", "owner_name", "owner_contact", "category", "image",
        )

        extra_kwargs = {
            "color": {"required": False, "allow_null": True, },
        }


class PetListSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()

    def get_category(self, instance: Pet):
        return instance.category.get_category_display()

    class Meta:
        model = Pet
        fields = (
            "id", "name", "age", "category", "image", "is_rented",
        )


class PetCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetCategory
        fields = ("category",)
