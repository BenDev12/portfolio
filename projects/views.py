from rest_framework import generics
from . import models
from . serialzer import ProjectSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .permissions import IsProjectOwnerOrReadOnly

# Create your views here.


class PostProject(generics.ListCreateAPIView):

    queryset = models.Project.postProjects.all()
    serializer_class = ProjectSerializer


class ViewProject(generics.RetrieveUpdateDestroyAPIView):

    queryset = models.Project.objects.all()
    serializer_class = ProjectSerializer

    def get(self, request, id):
        project = get_object_or_404(models.project, id=id)
        if not project:
            return Response({
                'errors':'Project with specified name does not exist'
            }, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, id):
        pass

    def delete(self, _, id):
        pass