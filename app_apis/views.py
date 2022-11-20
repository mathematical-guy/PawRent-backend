from rest_framework import generics
from app_apis.serializers import PetListAuthenticatedUserSerializer
from pet.models import Pet


class PetListView(generics.ListAPIView):
    serializer_class = PetListAuthenticatedUserSerializer
    queryset = Pet.objects.all()
