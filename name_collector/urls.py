from django.urls import path

from . import views

app_name = 'name_collector'
urlpatterns = [
    path('', views.index, name='index'),
    path('userlist/', views.userlist, name='userlist')
]
