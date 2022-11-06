from pet.models import Pet, PetCategory
from pet.serializers import PetSerializer, PetCategoryListSerializer, PetListSerializer
from rest_framework import viewsets, generics


class PetCategoryListView(generics.ListAPIView):
    serializer_class = PetCategoryListSerializer
    queryset = PetCategory.objects.all()


class PetViewSet(viewsets.ModelViewSet):
    serializer_class = PetSerializer
    queryset = Pet.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return PetListSerializer

        return self.serializer_class
