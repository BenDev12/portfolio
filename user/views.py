from django.shortcuts import get_object_or_404
from rest_framework import status,generics
from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response

# Create your views here.

class userCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def post(self, *args, **kwargs):
        serializer = UserSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'User created sucessfully'})

class userDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_url_kwarg = 'id'

            
