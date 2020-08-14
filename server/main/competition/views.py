from rest_framework.generics import ListAPIView , RetrieveAPIView
from rest_framework.response import Response
from . serializers import AllCompetitionSerializer, CompetitionSerializer
from . models import Competition


class OngoingCompetitions(ListAPIView):
    serializer_class = AllCompetitionSerializer
    queryset = Competition.objects.filter(ended=False)


class EndedCompetitions(ListAPIView):
    serializer_class = AllCompetitionSerializer
    queryset = Competition.objects.filter(ended=True)


class AllCompetitions(ListAPIView):
    serializer_class = AllCompetitionSerializer
    queryset = Competition.objects.all()


class SingleCompetetion(RetrieveAPIView):
    lookup_field = 'id'
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer

