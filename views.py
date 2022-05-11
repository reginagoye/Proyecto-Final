from email import message
import http
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
from .models import Message
# from chat.forms import SignUpForm
# from chat.serializers import MessageSerializer, UserSerializer

# Create your views here.
# def index(request):
#     if request.User.is_authenticated:
#         return redirect('chats')
#     if request.method == 'GET':
#         return render(request, 'chat/index.html', {})
#     if request.method == "POST":
#         username, password = request.POST['username'], request.POST['password']
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             login(request, user)
#         else:
#             return HttpResponse('{"error": "User does not exist"}')
#         return redirect('chats')
 
 
 
@csrf_exempt
def message_list(request, sender=None, receiver=None):
    """
    List all required messages, or create a new message.
    """
    if request.method == 'GET':
        messages = Message.objects.filter(sender_id=sender, receiver_id=receiver, is_read=False).values()
        # serializer = MessageSerializer(messages, many=True, context={'request': request})
        # for message in messages:
        #     message.is_read = True
        #     message.save()
        return JsonResponse(messages, safe=False)
 
    # elif request.method == 'POST':
    #     data = JSONParser().parse(request)
    #     serializer = MessageSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data, status=201)
    #     return JsonResponse(serializer.errors, status=400)
 
 
 
def chat_view(request):
    if request.method == "GET":
        return render(request, 'chat.html',
                      {'users': User.objects.exclude(username=request.user.username)})
 
 
def message_view(request, sender, receiver):
    if request.method == "GET":
        return render(request, "messages.html",
                      {'users': User.objects.exclude(username=request.user.username),
                       'receiver': User.objects.get(id=receiver),
                       'messages': Message.objects.filter(sender_id=sender, receiver_id=receiver) |
                                   Message.objects.filter(sender_id=receiver, receiver_id=sender)})

def saludo(request):
    print(request.POST)
    print(request.GET)
    print(request.method)

    if User.objects.filter(username=request.POST.get("receptor")).exists():
        receptor=User.objects.get(username=request.POST["receptor"])
        mensaje=Message.objects.create(receiver=request.POST["receptor"], sender=request.POST["remitente"], message=request.POST["mensaje"])
        return HttpResponse('se ha enviado un mensaje al usuario'+receptor.username)
    else:
        return render(request, 'chat.html')

def saludo2(request):
    print(request.POST["receptor"])
    print(request.user.username)

    if User.objects.filter(username=request.POST["receptor"]).exists():
        receptor=User.objects.filter(username=request.POST["receptor"])[0]
        print(type(receptor))
        mensaje=Message.objects.create(receiver=receptor, sender=request.user, message=request.POST["mensaje"][0])
        return HttpResponse('se ha enviado un mensaje al usuario '+receptor.username)
    else:
        return render(request, 'chat.html')
