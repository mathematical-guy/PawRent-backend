from django.contrib import admin
from django.urls import path
from rest_framework import routers
from pet.views import PetViewSet, PetCategoryListView

router = routers.DefaultRouter()

router.register("", PetViewSet)


urlpatterns = [
    path("pet-categories/", PetCategoryListView.as_view(),),
]


urlpatterns += router.urls