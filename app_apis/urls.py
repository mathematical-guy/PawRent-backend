from django.urls import path
from app_apis.views import PetListView


urlpatterns = [
    path("pet-list/", PetListView.as_view()),
]
