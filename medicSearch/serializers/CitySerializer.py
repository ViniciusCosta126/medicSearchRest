from rest_framework import serializers
from medicSearch.models import City


class CitySerializer(serializers.ModelSerializer):
    state = serializers.StringRelatedField()
    class Meta:
        model = City
        fields = ['id','name','state']
