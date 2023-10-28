from django.contrib import admin
from django.urls import path, include
from medicSearch.views import login_view, register
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('medicSearch.urls')),
    path('login/', login_view, name='login'),
    path('register/', register, name='register')
]
