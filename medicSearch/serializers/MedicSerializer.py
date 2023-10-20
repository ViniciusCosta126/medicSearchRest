from rest_framework import serializers
from medicSearch.models import Profile

class MedicSerializer(serializers.ModelField):
    class Meta:
        model = Profile
        fields = '__all__'