from rest_framework import serializers
from medicSearch.models import Speciality


class SpeacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Speciality
        fields = ['id', 'name', 'status']
