from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from . models import Artist, Artwork
from . serializers import ArtistSerializer, ArtworkSerializer


class ArtworkCreateView(CreateAPIView):

    serializer_class = ArtworkSerializer
    queryset = Artwork.objects.all()



class ArtisCreateView(CreateAPIView):

    serializer_class = ArtistSerializer
    queryset = Artist.objects.all()


class ArtworktViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Artwork.objects.all()
        serializer = ArtworkSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Artwork.objects.all()
        artwork = get_object_or_404(queryset, id=pk)
        print(artwork.paid)
        serializer = ArtworkSerializer(artwork)
        return Response(serializer.data)

