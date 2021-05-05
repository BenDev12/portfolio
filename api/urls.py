from django.urls import path
from .views import Post , Details
app_name ='api'
urlpatterns=[
    path('<int:pk>/',Details.as_view(), name="viewDetails"),
    path('', Post.as_view(), name="listPost")
]