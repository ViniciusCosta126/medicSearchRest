from rest_framework import viewsets, filters
from medicSearch.models import Profile
from medicSearch.serializers import MedicSerializer
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend


class MedicPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page'
    max_page_size = 10


class MedicViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.filter(role=2)
    serializer_class = MedicSerializer
    pagination_class = MedicPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['user__first_name']
    filterset_fields = ['specialities__id', 'addresses__neighborhood',
                        'addresses__neighborhood__city', 'addresses__neighborhood__city__state']
