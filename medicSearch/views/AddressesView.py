from rest_framework import viewsets
from medicSearch.models import Address
from medicSearch.serializers import AddressesSerializer


class AddressesViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressesSerializer
    http_method_names = ['get']
