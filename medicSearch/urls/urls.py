from django.urls import path, include
from rest_framework.routers import DefaultRouter
from medicSearch.views import ProfileViewSet, MedicViewSet, AddressesViewSet, CitysViewSet, SpecialityViewSet, StateViewSet, NeighborhoodViewSet

router = DefaultRouter()
router.register('profiles', ProfileViewSet, basename="Perfis")
router.register('medics', MedicViewSet, basename='Medicos')
router.register('addresses', AddressesViewSet, basename='Enderecos')
router.register('citys', CitysViewSet, basename='Cidades')
router.register('specialities', SpecialityViewSet, basename='Especialidades')
router.register('states', StateViewSet, basename='Estados')
router.register('neighborhoods', NeighborhoodViewSet, basename='Enderecos')

urlpatterns = router.urls
