from django.db import models

# Create your models here.

class Track(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100, blank=True)
    genre = models.CharField(max_length=50, blank=True)
    release_date = models.DateField(null=True, blank=True)
    audio_file = models.FileField(upload_to='tracks/', blank=True)

    def __str__(self):
        return f"{self.title} - {self.artist}"