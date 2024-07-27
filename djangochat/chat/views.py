from django.shortcuts import render , redirect
from .models import *
from django.http import HttpResponse , JsonResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def room(request , room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request , 'room.html' , {
        'username' : username ,
        'room' : room ,
        'room_details' : room_details
    })

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name = room).exists():
        return redirect('/'+ room + '/?username=' + username)
    else:
        new_room = Room.objects.create(name = room)
        new_room.save()
        return redirect('/'+ room + '/?username=' + username)
    
def send(request):
    message = request.POST.get('message')
    username = request.POST.get('username')
    room_id = request.POST.get('room_id')

    try:
        room = Room.objects.get(id=room_id)
        new_message = Message.objects.create(value=message, user=username, room=room)
        return HttpResponse('Message envoyé avec succès')
    except Room.DoesNotExist:
        return HttpResponse('Room does not exist', status=400)
    except Exception as e:
        return HttpResponse(f'Error: {str(e)}', status=500)


def getMessages(request , room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room = room_details.id).order_by('date')
    return JsonResponse({"messages" :list(messages.values())})