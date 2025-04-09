from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth.models import User
from .serializer import UserSerializer
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404
from datetime import datetime
from .models import Profile

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({"detail": "Invalid credentials."}, status=status.HTTP_404_NOT_FOUND)

    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)

    # Ensure profile exists
    profile, created = Profile.objects.get_or_create(user=user)
    profile.lastseen = datetime.now()
    profile.save()

    return Response({
        "token": token.key,
        "user": serializer.data,
        "lastseen": profile.lastseen
    }, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()

        token = Token.objects.create(user=user)

        profile, created = Profile.objects.get_or_create(user=user)
        profile.lastseen = datetime.now()
        profile.save()

        return Response({
            "token": token.key,
            "user": serializer.data,
            "lastseen": profile.lastseen
        }, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
