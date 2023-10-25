from rest_framework import serializers
from medicSearch.models import DayWeek


class DayWeekSerializer(serializers.ModelSerializer):
    class Meta:
        model = DayWeek
        fields = ['id', 'name', 'status']
