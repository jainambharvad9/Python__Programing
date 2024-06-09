from django.shortcuts import render,redirect
from chatapp.models import Room,Message
from django.http import HttpResponse , JsonResponse
# Create your views here.


def home(request):
    return render(request, 'home.html') 

def room(request,room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html',{
        "username": username,
        'room':room,
        'room_details': room_details
    })

# def checkview(request):
#     room = request.POST.get('room_name')
#     username = request.POST.get('username')
    
#     if Room.objects.filter(name=room).exists():
#         return redirect('/'+ room +'/?username='+username)
#     else:
#         new_room = Room.objects.create(name=room)
#         new_room.save()
#         return redirect('/'+ room +'/?username='+username)

def checkview(request):
    room_name = request.POST.get('room_name')
    username = request.POST.get('username')

    if Room.objects.filter(name=room_name).exists():
        return redirect(f'/{room_name}/?username={username}')
    else:
        new_room = Room.objects.create(name=room_name)
        new_room.save()
        return redirect(f'/{room_name}/?username={username}')
    
    
def send(request):
    message = request.POST.get('message')
    username = request.POST.get('username')
    room_id = request.POST.get('room_id')
    
    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message send successfully')


def getMessages(request,room):
    room_details = Room.objects.get(name=room)
    
    message  = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(message.values())})