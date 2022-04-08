from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Music
from.serializers import MusicSerializer
from music import serializers

@api_view(['GET'])
def musics_list(request):
    musics = Music.objects.all()

    serializer = MusicSerializer(musics, many=True)

    
    return Response(serializer.data)
