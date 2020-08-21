from django.db.models import Prefetch
from rest_framework.generics import ListAPIView , RetrieveAPIView
from rest_framework.response import Response
from . serializers import AllCompetitionSerializer, CompetitionSerializer
from . models import Competition
from submission.models import Artwork

class OngoingCompetitions(ListAPIView):
    serializer_class = AllCompetitionSerializer
    queryset = Competition.objects.filter(ended=False).prefetch_related(
        Prefetch(
            'artworks',
            queryset=Artwork.objects.filter(approved=True, paid=True)
        )
    )


class EndedCompetitions(ListAPIView):
    serializer_class = AllCompetitionSerializer
    queryset = Competition.objects.filter(ended=True).prefetch_related(
        Prefetch(
            'artworks',
            queryset=Artwork.objects.filter(approved=True, paid=True)
        )
    )


class AllCompetitions(ListAPIView):
    serializer_class = AllCompetitionSerializer
    queryset = Competition.objects.prefetch_related(
        Prefetch(
            'artworks',
            queryset=Artwork.objects.filter(approved=True, paid=True)
        )
    )


class SingleCompetetion(RetrieveAPIView):
    lookup_field = 'id'
    queryset = Competition.objects.prefetch_related(
        Prefetch('artworks',
                 queryset=Artwork.objects.filter(approved=True, paid=True)
        )
    )
    serializer_class = CompetitionSerializer

