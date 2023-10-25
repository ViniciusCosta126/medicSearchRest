from rest_framework import serializers
from medicSearch.models import Address


class AddressesSerializer(serializers.ModelSerializer):
    neighborhood = serializers.StringRelatedField()
    days_week = serializers.StringRelatedField(many=True)

    class Meta:
        model = Address
        fields = ['neighborhood', 'days_week', 'address',
                  'cep', 'opening_time', 'closing_time', 'phone']
