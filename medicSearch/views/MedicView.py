from rest_framework import viewsets, filters
from medicSearch.models import Profile
from medicSearch.serializers import MedicSerializer
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django.http import HttpResponseRedirect
import django_filters


class MedicPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page'
    max_page_size = 10


class MedicFilter(django_filters.FilterSet):
    # Renomeie os campos que deseja usar para filtrar
    speciality = django_filters.CharFilter(
        field_name='specialities__id', lookup_expr='iexact')
    neighborhood = django_filters.CharFilter(
        field_name='addresses__neighborhood', lookup_expr='iexact')
    city = django_filters.CharFilter(
        field_name='addresses__neighborhood__city',)
    state = django_filters.CharFilter(
        field_name='addresses__neighborhood__city__state',)

    class Meta:
        model = Profile
        fields = []


class MedicViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            # Redireciona para a página de login
            return HttpResponseRedirect('/login/')
        return super().dispatch(request, *args, **kwargs)
    queryset = Profile.objects.filter(role=2)
    serializer_class = MedicSerializer
    pagination_class = MedicPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['user__first_name']
    filterset_class = MedicFilter
