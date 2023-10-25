from rest_framework import serializers
from medicSearch.models import Neighborhood


class NeighborhoodSerializer(serializers.ModelSerializer):
    city = serializers.StringRelatedField()
    class Meta:
        model = Neighborhood
        fields = ['id','name','status','city']