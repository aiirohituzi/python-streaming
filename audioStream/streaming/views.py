from django.shortcuts import render
import os
from django.http import HttpResponse
from rest_framework import viewsets
from streaming.serializers import AudiosSerializer
from streaming.forms import AudiosForm
from django.views.decorators.csrf import csrf_exempt

from streaming.models import Audios


class AudiosViewSet(viewsets.ModelViewSet):  
    queryset = Audios.objects.all().order_by('-id')
    serializer_class = AudiosSerializer

def getAudio(request):
    fname = os.path.abspath(os.path.join('../music', "Intro.mp3"))
    f = open(fname, 'rb')

    response = HttpResponse()
    response.write(f.read())
    response['Content-Type'] = 'audio/mp3'
    response['Content-Length'] = os.path.getsize(fname)

    return response

@csrf_exempt
def upload(request):
    result = False

    print(request.FILES)
    audiosForm = AudiosForm(request.POST, request.FILES)
    print(audiosForm)

    if audiosForm.is_valid():
        obj = audiosForm.save(commit=False)
        obj.save()
        result = True


    print(result)
    return HttpResponse(result)



@csrf_exempt
def delete(request):
    result = False
    log = ''
    musicId = request.POST['id']

    try:
        row = Audios.objects.get(id=musicId)
    except Audios.DoesNotExist:
        print("Delete Request : [Failed]No Audios matches the given query.")
        return HttpResponse(result)
    
    if row != None:
        log += 'Delete Request : ' + str(row.id) + ' music delete success'
        print(log)
        row.delete()
        result = True
    else:
        print("Delete Request : Delete error")

    return HttpResponse(result)