from django.urls import re_path as urls
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    urls('testimoni/', TestimoniView.as_view(), name="TestimoniView"),
]

urlpatterns = format_suffix_patterns(urlpatterns)