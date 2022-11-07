from rest_framework import viewsets
from account_management.serializers import AddContractSerializer
from account_management.models import Contract, User


class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = AddContractSerializer
