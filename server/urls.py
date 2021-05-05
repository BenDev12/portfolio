
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('blog/', include('api.urls', namespace='api')),
    path('project/', include('projects.urls', namespace='projects'))
]
