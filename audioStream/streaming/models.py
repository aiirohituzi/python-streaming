from django.db import models

from smartfields import fields

# Create your models here.
class Audios(models.Model):
    music = fields.FileField(upload_to='music/')

    class Meta:
        ordering = ('id',)