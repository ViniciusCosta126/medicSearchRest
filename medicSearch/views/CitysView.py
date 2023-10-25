from medicSearch.models import City
from medicSearch.serializers import CitySerializer
from rest_framework import viewsets


class CitysViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    http_method_names = ['get']