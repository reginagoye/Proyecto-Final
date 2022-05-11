
from django.urls import path
from . import views
 
 
urlpatterns = [
    
    path('chat/', views.chat_view, name='chats'),
    path('chat/<int:sender>/<int:receiver>/', views.message_view, name='chat'), 
    path('api/messages/<int:sender>/<int:receiver>/', views.message_list, name='message-detail'),
    path('api/messages/', views.message_list, name='message-list'),
    path('saludo/', views.saludo, name='saludo'),
    path('saludo2/', views.saludo2, name='saludo2')
]