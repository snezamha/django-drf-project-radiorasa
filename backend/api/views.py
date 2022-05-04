from rest_framework.generics import ListAPIView
from audio.models import Audio
from .serializers import AudioSerializer
# Create your views here.


class AudioList(ListAPIView):
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer
