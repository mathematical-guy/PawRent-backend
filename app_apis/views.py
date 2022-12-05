from rest_framework import generics, viewsets
from app_apis.serializers import PetListAuthenticatedUserSerializer, PetDetailSerializer
from pet.models import Pet
from pet.choices import PET_CATEGORY_CHOICES
from pet.constants import PetCategoryConstants
from backend.constants import RequestMethods, RequestActions


class PetListView(generics.ListAPIView):
    serializer_class = PetListAuthenticatedUserSerializer
    queryset = Pet.objects.all()


class PetDetailView(generics.RetrieveAPIView):
    serializer_class = PetDetailSerializer
    queryset = Pet.objects.all()


class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()

    def get_serializer_class(self):
        if self.action == RequestActions.RETRIEVE:
            return PetDetailSerializer
        return PetListAuthenticatedUserSerializer
