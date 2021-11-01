from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nova_transacao/', views.nova_transacao, name='nova_transacao'),
    path('up_transacao/<int:pk>', views.up_transacao, name='up_transacao'),
    path('del_transacao/<int:pk>', views.del_transacao, name='del_transacao'),
                    
]