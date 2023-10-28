from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import login, authenticate
from medicSearch.models import Profile
from medicSearch.serializers import UserSerializer,ProfileSerializer


@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        user_serializer = UserSerializer(data=request.data)
        profile_serializer = ProfileSerializer(data=request.data)
        if user_serializer.is_valid():
            user  = user_serializer.save()
            user.set_password(request.data['password'])
            user.save()
            return Response({'message': 'Registrado com sucesso'}, status=status.HTTP_201_CREATED)
        return Response({'message': 'Registro falhou', 'errors': profile_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_view(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            profile = Profile.objects.get(user=user)
            return Response({'message': 'Loggado com sucesso', 'user_profile': ProfileSerializer(profile).data})
        return Response({'message': 'Credenciais invalidas por favor verifique'}, status=status.HTTP_401_UNAUTHORIZED)
