from django.shortcuts import render
from django.shortcuts import redirect
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

    response = HttpResponse()
    responseSize = 0

    id = request.GET.get('id', False)

    if(id):
        print(id)
        row = Audios.objects.get(id=request.GET['id'])
        
        split_path = str(row.music).split('/')
        filename = split_path[len(split_path)-1]
        fname = os.path.abspath(os.path.join('./music', filename))
        f = open(fname, 'rb')
        response.write(f.read())
        f.close()
        responseSize += os.path.getsize(fname)

    else:
        for rows in Audios.objects.all():
            print(rows.music)
            split_path = str(rows.music).split('/')
            filename = split_path[len(split_path)-1]

            fname = os.path.abspath(os.path.join('./music', filename))
            responseSize += os.path.getsize(fname)
            print(responseSize)

            f = open(fname, 'rb')
            response.write(f.read())
            f.close()

    response['Content-Type'] = 'audio/mp3'
    response['Content-Length'] = responseSize

    return response



def selectGetAudio(request):

    response = HttpResponse()
    responseSize = 0

    id_str = request.GET.get('id', False)

    id_list = id_str.split(',')
    
    for id in id_list:
        # print(id)
        row = Audios.objects.get(id=id)
        
        split_path = str(row.music).split('/')
        filename = split_path[len(split_path)-1]
        fname = os.path.abspath(os.path.join('./music', filename))
        f = open(fname, 'rb')
        response.write(f.read())
        f.close()
        responseSize += os.path.getsize(fname)
        # print(fname)
        # print(responseSize)

    response['Content-Type'] = 'audio/mp3'
    response['Content-Length'] = responseSize

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
    if(request.method == 'POST'):
        musicId = request.POST['id']
    elif(request.method == 'GET'):
        musicId = request.GET['id']

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

    return redirect('music_list')
    # return HttpResponse(result)



def musicList(request):
    musics = Audios.objects.all().order_by('id')
    return render(request, 'music_list.html', {'musics': musics})



def musicUpload(request):
    if request.method == "POST":
        form = AudiosForm(request.POST, request.FILES)
        # print(form.is_valid())
        # print(request.FILES['music'])

        split_fname = str(request.FILES['music']).split('.')
        extension = split_fname[len(split_fname)-1]
        # print(extension)

        # if(extension == 'mp3'):
        #     print("asdfasdfasdf")

        if form.is_valid() and extension == 'mp3':
            obj = form.save(commit=False)
            obj.save()
            print("success")
            return redirect('music_list')
    else:
        form = AudiosForm()
    return render(request, 'music_upload.html', {'form': form})



def randomPlay(request):

    response = HttpResponse()
    responseSize = 0

    for rows in Audios.objects.all().order_by('?'):
        print(rows.id)
        print(rows.music)
        split_path = str(rows.music).split('/')
        filename = split_path[len(split_path)-1]

        fname = os.path.abspath(os.path.join('./music', filename))
        responseSize += os.path.getsize(fname)
        # print(responseSize)

        f = open(fname, 'rb')
        response.write(f.read())
        f.close()

    response['Content-Type'] = 'audio/mp3'
    response['Content-Length'] = responseSize

    return response