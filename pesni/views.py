from django.shortcuts import render
from . import models
from rest_framework import viewsets
from rest_framework import filters
from . import serializers


class TrackViewSet(viewsets.ModelViewSet):
	queryset = models.Track.objects.all()
	serializer_class = serializers.TrackSerializer
	filter_backends = [filters.SearchFilter]
	search_fields = ['name', 'singer__name']

class SingerViewSet(viewsets.ModelViewSet):
	queryset = models.Singer.objects.all()
	serializer_class = serializers.SingerSerializer
	filter_backends = [filters.SearchFilter]
	search_fields = ['name']

class GenreViewSet(viewsets.ModelViewSet):
	queryset = models.Genre.objects.all()
	serializer_class = serializers.GenreSerializer
