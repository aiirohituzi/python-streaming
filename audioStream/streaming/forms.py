from __future__ import unicode_literals

from django import forms

from .models import Audios

class AudiosForm(forms.ModelForm):
    class Meta:
        model = Audios
        fields = ('music', )