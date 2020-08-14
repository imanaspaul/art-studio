from rest_framework import serializers
from . models import Artist, Artwork

class ArtistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = "__all__"



class ArtworkSerializer(serializers.ModelSerializer):
    # artwork_artist = ArtistSerializer()
    class Meta:
        model = Artwork
        fields = "__all__"
        depth = 1