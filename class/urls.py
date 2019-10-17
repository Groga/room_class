from django.urls import path
from django.urls import include
from .views import index_class


urlpatterns = [
    path('', index_class, name='index_class'),
]