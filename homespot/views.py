from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.parsers import MultiPartParser, JSONParser
from .etc.getuuid import get_id
from .etc.response_get import response
from .serializer import *
from rest_framework.views import APIView
from django.conf import settings
import json
from . import models
from rest_framework import status
from datetime import datetime
# Create your views here.

class TestimoniView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        get_testimoni = TestimoniSerializer(Testimoni.objects.all().order_by("-id"), many=True)

        self.data = {
            "testimoni": get_testimoni.data
        }

        return response(code=200, data=self.data, detail_message="")
    
    def post(self, request):
        name = request.data['name']
        jabatan = request.data['jabatan']
        rating = request.data['rating']
        message = request.data['message']
        image = request.FILES.get('image', None)

        try:
            Testimoni.objects.create(id_testimoni=get_id(), name=name, jabatan=jabatan, rating=int(rating), message=message, image=None if image == 'null' else image)

            return response(code=201, data=None, detail_message='Created request success')
        except Exception as e:
            print(e)
            return response(code=500, data="", detail_message="error!")
