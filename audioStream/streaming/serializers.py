from django.forms import widgets  
from rest_framework import serializers  
from streaming.models import Audios

class AudiosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Audios
        fields = ('id', 'music')    