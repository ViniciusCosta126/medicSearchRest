from rest_framework import viewsets
from medicSearch.models import Profile
from medicSearch.serializers import MedicSerializer


class MedicViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = MedicSerializer
