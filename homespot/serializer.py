from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from .models import *

class TestimoniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimoni
        exclude = ['id']

