from django.urls import path
from . import views
urlpattrens = [
    path('', views.index, name='index'),
    path('<str:name>', views.greet, name='greet')
    
]