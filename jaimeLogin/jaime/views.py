from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import UserSerializer
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth.models import User

@api_view(['POST'])
def login(request):
    return Response ({})

@api_view(['POST'])
def signup(request):
    serialize = UserSerializer(data=request.data)
    if serialize.is_valid():
        serialize.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({"token":token.key,"user": serialize.data})
    return Response (serialize.errors,status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def test_token(request):
    return Response ({})