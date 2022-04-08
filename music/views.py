from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Music
from.serializers import MusicSerializer

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
    
    
