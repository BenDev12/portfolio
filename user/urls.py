from django.urls import path
from .views import userCreateAPIView

urlpatterns=[
    path('', userCreateAPIView.as_view(), name='user'),

]
