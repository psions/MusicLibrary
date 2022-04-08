from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework.response import Response
from rest_framework import status
from .models import Music
from.serializers import MusicSerializer
from music import serializers
from .models import Post, Like

@api_view(['GET', 'POST'])
def musics_list(request):
    
    if request.method == 'GET':
        musics = Music.objects.all()
        serializer = MusicSerializer(musics, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MusicSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT','DELETE'])   
def music_detail(request, pk):
    music = get_object_or_404(Music, pk=pk)
    if request.method == 'GET':
        serializer = MusicSerializer(music);
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer= MusicSerializer(music, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        music.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def post_view(request):
    qs = Post.objects.all()
    user = request.user

    context = {
        'qs': qs,
        'user': user,
    }

    return render(request, 'posts/main.html', context)

def like_post(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id=post_id)

        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
        else:
            post_obj.liked.add(user)

        like, created = Like.objects.get_or_create(user=user, post_id=post_id)

        if not created:
            if like.value == 'Like':
                like.value= 'Unlike'
            else:
                like.value == 'Like'

        like.save()
    return redirect('posts:post-list')


    
    
