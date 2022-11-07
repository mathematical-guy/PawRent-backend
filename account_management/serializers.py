from rest_framework import serializers
from account_management.models import User, Contract


class AddContractSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(
        slug_field="username", queryset=User.objects.all(),
        error_messages={'does_not_exist': "User with username {value} does not exists"}
    )
    renter = serializers.SlugRelatedField(
        slug_field="username", queryset=User.objects.all(),
        error_messages={'does_not_exist': "User with username {value} does not exists"}
    )

    class Meta:
        model = Contract
        fields = ("id", "owner", "renter", "duration",)
        extra_kwargs = {
            "duration": {"required": True,}
        }

    def validate_owner(self, owner: User):
        if not owner.is_pet_available:
            raise serializers.ValidationError("Pet not available for selected Owner")
        return owner

    def create(self, validated_data):
        validated_data["is_active"] = True
        return super(AddContractSerializer, self).create(validated_data)
