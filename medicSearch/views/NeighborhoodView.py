from rest_framework import viewsets
from medicSearch.models import Neighborhood
from medicSearch.serializers import NeighborhoodSerializer


class NeighborhoodViewSet(viewsets.ModelViewSet):
    queryset = Neighborhood.objects.all()
    serializer_class = NeighborhoodSerializer
    http_method_names = ['get']