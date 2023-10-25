from django.urls import path, include
from rest_framework.routers import DefaultRouter
from medicSearch.views import ProfileViewSet, MedicViewSet, AddressesViewSet

router = DefaultRouter()
router.register('profiles', ProfileViewSet, basename="Perfis")
router.register('medics', MedicViewSet, basename='Medicos')
router.register('addresses', AddressesViewSet, basename='Enderecos')


urlpatterns = router.urls
