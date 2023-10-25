from django.urls import path, include
from rest_framework.routers import DefaultRouter
from medicSearch.views import ProfileViewSet, MedicViewSet, AddressesViewSet, CitysViewSet

router = DefaultRouter()
router.register('profiles', ProfileViewSet, basename="Perfis")
router.register('medics', MedicViewSet, basename='Medicos')
router.register('addresses', AddressesViewSet, basename='Enderecos')
router.register('citys', CitysViewSet, basename='Cidades')


urlpatterns = router.urls
