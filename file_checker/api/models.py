from django.db import models


class MusicFile(models.Model):
    title = models.CharField('имя файла', max_length=100)
    file = models.FileField('файл', upload_to='music_files/')

    class Meta:
        verbose_name = 'Музыкальный файл'
        verbose_name_plural = 'Музыкальные файлы'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.title = self.file.name
        super().save(*args, **kwargs)
