from django.shortcuts import render
import os
from django.http import HttpResponse

# Create your views here.
def getAudio(request):
    fname = os.path.abspath(os.path.join('../music', "Intro.mp3"))
    f = open(fname, 'rb')

    response = HttpResponse()
    response.write(f.read())
    response['Content-Type'] = 'audio/mp3'
    response['Content-Length'] = os.path.getsize(fname)

    return response