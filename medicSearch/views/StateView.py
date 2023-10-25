from rest_framework import viewsets
from medicSearch.serializers import StateSerializer
from medicSearch.models import State


class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    http_method_names = ['get']
