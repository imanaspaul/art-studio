from django.urls import path
from . views import ArtworkCreateView, ArtisCreateView



urlpatterns = [
    path('call-for-artist/', ArtworkCreateView.as_view()),
    path('create-artist/', ArtisCreateView.as_view()),
]
