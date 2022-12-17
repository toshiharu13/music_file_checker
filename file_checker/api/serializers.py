from rest_framework import serializers
from .models import MusicFile

class FileSerializer(serializers.ModelSerializer):
  class Meta():
    model = MusicFile
    fields = ('file',)