from rest_framework import serializers
from . models import Artist, Artwork

class ArtistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = [
            "id", 
            "full_name", 
            "email", 
            "artist_website",
            "artist_biography", 
            "artist_statement"
        ]



class ArtworkSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer()
    class Meta:
        model = Artwork
        fields = [
            "id",
            "title",
            "medium",
            "dimension",
            "paid",
            "approved",
            "user",
            "position",
            "artist"
        ]
