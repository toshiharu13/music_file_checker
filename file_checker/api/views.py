import soundfile as sf
from django.shortcuts import get_object_or_404, render
from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import MusicFile
from .serializers import FileSerializer
from .validators import validate_music_file


class GetFile(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        MusicFile.objects.all().delete()
        uploaded_file_name = request.FILES['file'].name
        serializer = FileSerializer(data=request.data)

        if serializer.is_valid():
            if validate_music_file(uploaded_file_name):
                serializer.save()
            else: return Response('Не верное расширение файла')

            music_file_object = get_object_or_404(
                MusicFile, title=uploaded_file_name)
            music_file_path = music_file_object.file.path
            try:
                data, samplerate = sf.read(music_file_path)
                return Response('Формат корректен', status=status.HTTP_200_OK)
            except sf.LibsndfileError as err:
                return Response(
                    'Ошибка чтения, проверьте формат и целостность файла')

        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
