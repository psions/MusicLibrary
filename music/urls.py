from django.urls import path
from . import views

app_name= 'posts'

urlpatterns = [
    path('', views.musics_list),
    path('<int:pk>/', views.music_detail),
   
]