import uuid
from django.db import models
from django.conf import settings

from competition.models import Competition

class Artist(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=255, verbose_name='Full Name')
    email = models.EmailField(max_length=254)
    artist_website = models.URLField(verbose_name="Artist's website")
    artist_biography = models.TextField(verbose_name="Artist's biography")
    artist_statement = models.TextField(verbose_name="Artist's statement")

    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.full_name


    class Meta:
        verbose_name_plural = "Artists"
    

class Artwork(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, verbose_name="Artwork title")
    medium = models.CharField(max_length=100)
    dimension = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="artwork_artist")
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE, related_name="artworks")
    paid = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)
    user = models.CharField(max_length=255, blank=True, null=True)
    position = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name_plural = "Artworks"
