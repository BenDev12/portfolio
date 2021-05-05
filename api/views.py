from rest_framework import generics 
from . import models
from .serializer import PostSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

# Create your views here.


class Post(generics.ListCreateAPIView):

    queryset = models.Post.postObjects.all()
    serializer_class = PostSerializer


class Details(generics.RetrieveUpdateDestroyAPIView):

    queryset = models.Post.objects.all()
    serializer_class = PostSerializer
