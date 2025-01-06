# from django.urls import path
# from . import views




# urlpatterns = [
#     path('new/', views.new, name='new'),
#     path('<int:pk>/',views.detail, name='detail'),
# ]


# item/urls.py
from django.urls import path
from .views import detail, new  ,delete,edit, items,chat_view, send_message,delete_message

app_name='item'

urlpatterns = [
    path('',items,name='items'),
    path('item/<int:pk>/', detail, name='detail'),
    path('<int:pk>/delete/',delete,name='delete'),
    path('<int:pk>/edit/',edit,name='edit'),
    path('new/', new, name='new'), 
    path('chat/', chat_view, name='chat'),
    path('send-message/', send_message, name='send_message'),
    path('message/<int:message_id>/delete/', delete_message, name='delete_message'),
    path('chat/delete/<int:message_id>/', delete_message, name='delete_message'),
    
    
    
    path('<int:pk>/', detail, name='detail') ,
    
]


