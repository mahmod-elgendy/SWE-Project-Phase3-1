from rest_framework import serializers
from .models import MentorProfile, MenteeProfile, Match

class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentorProfile
        fields = '__all__'

class MenteeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenteeProfile
        fields = '__all__'

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'