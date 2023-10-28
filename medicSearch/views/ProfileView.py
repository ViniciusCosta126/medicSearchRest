from rest_framework import viewsets
from medicSearch.models import Profile
from medicSearch.serializers import ProfileSerializer
from rest_framework.permissions import IsAuthenticated

class ProfileViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
