from rest_framework import serializers
from medicSearch.models import State


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ['id', 'name', 'status']
