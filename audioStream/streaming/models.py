from django.db import models

# Create your models here.
class Audios(models.Model):
    music = models.FileField(upload_to='music/')

    class Meta:
        ordering = ('id',)