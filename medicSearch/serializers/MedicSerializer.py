from rest_framework import serializers
from medicSearch.models import Profile

class MedicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'