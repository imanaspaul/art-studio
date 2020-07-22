from rest_framework.generics import CreateAPIView
from rest_framework import viewsets
from . models import Artist, Artwork
from . serializers import ArtistSerializer, ArtworkSerializer


class ArtworkCreateView(CreateAPIView):

    serializer_class = ArtworkSerializer
    queryset = Artwork.objects.all()



class ArtisCreateView(CreateAPIView):

    serializer_class = ArtistSerializer
    queryset = Artist.objects.all()

