from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('name_collector/', include('name_collector.urls')),
    path('admin/', admin.site.urls),
]
