from . import models
import random
from rest_framework import serializers



class SingerSerializer(serializers.HyperlinkedModelSerializer):
	image = serializers.ImageField(use_url=False)

	class Meta:
		model = models.Singer
		fields = ['url', 'name', 'image', 'biography']

class TrackSerializer(serializers.HyperlinkedModelSerializer):
	#singer = SingerSerializer(read_only=True, many=True)
	singer = serializers.SerializerMethodField("singers_pretty")
	file = serializers.FileField(use_url=False)
	#genre = GenreSerializer()
	genre = serializers.CharField(source="genre.name")
	short_file = serializers.FileField(use_url=False, read_only=True)

	def singers_pretty(self, obj):
		return ', '.join([x.name for x in obj.singer.all()])

	class Meta:
		model = models.Track
		fields = ['url', 'singer', 'genre', 'name', 'file', 'short_file', 'start', 'end']

class GenreSerializer(serializers.HyperlinkedModelSerializer):
	default_singer_image_url = '/media/nothing.png'
	image = serializers.SerializerMethodField('get_random_singer_image')
	count = serializers.SerializerMethodField('count_of_tracks')
	singers = serializers.SerializerMethodField('singers_pretty')

	def singers_pretty(self, obj):
		return ', '.join([x.name for x in obj.singers.all()])

	def count_of_tracks(self, obj):
		return obj.track_set.count()

	def get_random_singer_image(self, obj):
		try:
			image = random.choice(random.choice(obj.track_set.all()).singer.all()).image.url
		except:
			image = self.default_singer_image_url
		return image
		

	class Meta:
		model = models.Genre
		fields = ['url', 'name', 'image', 'count', 'singers']
			