from rest_framework import viewsets
from medicSearch.models import Profile
from medicSearch.serializers import ProfileSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
