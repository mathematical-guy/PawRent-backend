from django.urls import path
from rest_framework import routers
from account_management.views import ContractViewSet

router = routers.DefaultRouter()

router.register("contracts", ContractViewSet)


urlpatterns = []

urlpatterns += router.urls
