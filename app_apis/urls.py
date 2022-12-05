from django.urls import path
from app_apis.views import PetListView, PetDetailView, PetViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register("pets", PetViewSet, basename="pets")

urlpatterns = [
    path("pet-list/", PetListView.as_view()),
    path("pet/<int:pk>/", PetDetailView.as_view()),
]

urlpatterns += router.urls
