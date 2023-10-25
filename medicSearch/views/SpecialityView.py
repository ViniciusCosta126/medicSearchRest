from rest_framework import viewsets
from medicSearch.models import Speciality
from medicSearch.serializers import SpeacilitySerializer


class SpecialityViewSet(viewsets.ModelViewSet):
    queryset = Speciality.objects.all()
    serializer_class = SpeacilitySerializer
    http_method_names = ['get']