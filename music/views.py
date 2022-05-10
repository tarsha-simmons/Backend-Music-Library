from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Music
from .serializer import Musicserializer


@api_view(['GET'])
def music_list(request):
    music = Music.objects.all()

    serializer = Musicserializer(music, many=True)

    return Response(serializer.data)