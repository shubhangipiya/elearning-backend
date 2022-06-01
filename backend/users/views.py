from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CustomUserSerializer
from rest_framework.permissions import AllowAny
from rest_framework import generics
from users.models import NewUser
from .models import NewUser as user_model
from rest_framework.permissions import IsAuthenticated
from users import models

from users import serializers


class CustomUserCreate(generics.CreateAPIView):
    queryset = NewUser.objects.all()
    serializer_class = CustomUserSerializer

    permission_classes = [AllowAny]

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetCurrentUser (generics.ListAPIView):
    serializer_class = CustomUserSerializer

    def get_queryset(self):
        user = self.request.user.id
        return NewUser.objects.filter(id=user)
