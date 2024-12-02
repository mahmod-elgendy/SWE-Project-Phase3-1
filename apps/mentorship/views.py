from rest_framework import viewsets
from .models import MentorProfile, MenteeProfile, Match
from .serializers import MentorSerializer, MenteeSerializer, MatchSerializer

class MentorViewSet(viewsets.ModelViewSet):
    queryset = MentorProfile.objects.all()
    serializer_class = MentorSerializer

class MenteeViewSet(viewsets.ModelViewSet):
    queryset = MenteeProfile.objects.all()
    serializer_class = MenteeSerializer

class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer