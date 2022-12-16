from django.urls import path
from .views import GetFile


urlpatterns = [
    path('v1/upload/', GetFile.as_view(), name='get_file'),
]