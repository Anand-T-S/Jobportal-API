from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from Users.serializers import RegistrationSerializer, LoginSerializer
from Users.models import User
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

# Create your views here.


class UserViewSet(ViewSet):
    def create(self, request, *args, **kwargs):
        # queryset = User.objects.all()
        serializer = RegistrationSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save()
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        queryset = User.objects.all()
        serializer = LoginSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            username = serializer.validated_data.get("username")
            password = serializer.validated_data.get("password")
            user = authenticate(request, username=username, password=password)
            if not user:
                return Response({"msg": "invalid credentials"})
            login(request, user)
            return Response({"msg": "login success"})
