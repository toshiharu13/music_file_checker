from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

from .serializers import FileSerializer
from .validators import validate_music_file


class GetFile(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        uploaded_file_ext = request.FILES['file'].name
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            if validate_music_file(uploaded_file_ext):
                serializer.save()
                print(uploaded_file_ext)
                return Response('Формат корректен', status=status.HTTP_200_OK)
            else: return Response('Не верное расширение файла')
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)