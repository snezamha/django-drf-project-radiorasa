from rest_framework.generics import ListAPIView
from radio.models import Audio
from .serializers import AudioSerializer
# Create your views here.


class AudioList(ListAPIView):
    queryset = Audio.objects.all().order_by('sort')
    serializer_class = AudioSerializer
