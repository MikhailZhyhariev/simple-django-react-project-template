from django.urls import path, re_path
from django.conf import settings
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
]
