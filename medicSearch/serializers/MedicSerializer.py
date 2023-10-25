from rest_framework import serializers
from medicSearch.models import Profile
from medicSearch.serializers import AddressesSerializer


class MedicSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    specialities = serializers.StringRelatedField(many=True)
    addresses = AddressesSerializer(read_only=True, many=True)

    class Meta:
        model = Profile
        fields = ['id', 'birthday', 'token', 'image',
                  'user', 'specialities', 'addresses',]
