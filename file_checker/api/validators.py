import os.path
from django.conf import settings

def validate_music_file(filename):
    _, ext = os.path.splitext(filename)
    print(ext, settings.MUSIC_EXT)
    return ext == settings.MUSIC_EXT