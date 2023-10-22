from rest_framework import viewsets
from medicSearch.models import Profile
from medicSearch.serializers import MedicSerializer
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


class MedicPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page'
    max_page_size = 1


class MedicViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.filter(role=2)
    serializer_class = MedicSerializer
    pagination_class = MedicPagination

    def list(self, request):
        medics = Profile.objects.filter(role=2)
        name = self.request.query_params.get('name')
        speciality = self.request.query_params.get('speciality')
        city = self.request.query_params.get('city')
        state = self.request.query_params.get('state')
        neighborhood = self.request.query_params.get('neighborhood')

        if name is not None and name != '':
            print(name)
            medics = medics.filter(user__first_name__contains=name)

        if speciality is not None:
            medics = medics.filter(specialities__id=speciality)

        if neighborhood is not None:
            medics = medics.filter(addresses__neighborhood=neighborhood)

        else:
            if city is not None:
                medics = medics.filter(addresses__neighborhood__city=city)
            elif state is not None:
                medics = medics.filter(addresses__neighborhood_state=state)

        serializer = self.get_serializer(medics, many=True)
        return Response(serializer.data)
