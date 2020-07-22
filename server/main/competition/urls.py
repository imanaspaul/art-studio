from django.urls import path
from . views import OngoingCompetitions, EndedCompetitions, AllCompetitions


urlpatterns = [
    path('all-competitions/', AllCompetitions.as_view()),
    path('ongoing-competitions/', OngoingCompetitions.as_view()),
    path('ended-competitions/', EndedCompetitions.as_view()),
]
