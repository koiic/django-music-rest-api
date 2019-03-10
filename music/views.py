from django.shortcuts import render
from rest_framework import generics

from music.models import Songs
from music.serializers import SongsSerializer


class ListSongsView(generics.ListAPIView):
	"""
	Provides a get method handler.
	"""
	queryset = Songs.objects.all()
	serializer_class = SongsSerializer