from django.db import models
from django.contrib.auth.models import User

class MentorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact = models.TextField()
    availability = models.TextField()
