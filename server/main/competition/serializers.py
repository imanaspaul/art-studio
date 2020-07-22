from rest_framework import serializers
from . models import Competition
from submission.serializers import ArtworkSerializer



class AllCompetitionSerializer(serializers.ModelSerializer):

    # artworks = serializers.StringRelatedField(many=True)
    artworks = ArtworkSerializer(many=True)

    class Meta:
        model = Competition
        fields = ["id", "name", "description", "thumnail", "created_at", "ended", "artworks"]

    # def get_artworks(self, obj):
    #     return artworks.objects.all()
