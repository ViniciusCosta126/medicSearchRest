from rest_framework import viewsets
from medicSearch.models import DayWeek
from medicSearch.serializers import DayWeekSerializer


class DayWeekViewSet(viewsets.ModelViewSet):
    queryset = DayWeek.objects.all()
    serializer_class = DayWeekSerializer
    http_method_names = ['get']
