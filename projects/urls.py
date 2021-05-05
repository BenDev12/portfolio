from django.urls import path
from .views import PostProject, ViewProject

app_name='projects'

urlpatterns=[
    path('',PostProject.as_view(), name='list_projects'),

    path('<int:pk>', ViewProject.as_view(), name='single_project')
]