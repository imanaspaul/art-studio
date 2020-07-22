from rest_framework.generics import ListAPIView
from . serializers import AllCompetitionSerializer
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
