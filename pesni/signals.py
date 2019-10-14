from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.files import File
from . import models
from pydub import AudioSegment
from threading import Thread
import os

@receiver(post_save, sender=models.Track)
def create_short_track(sender, instance, **kwargs):
	if instance.end != 0 and instance.short_file.name == '' or instance.short_file.name == None:
		song = AudioSegment.from_mp3(instance.file.url[1:])
		result = song[instance.start * 1000:instance.end * 1000]
		path = instance.file.url[1:].replace('music', 'short_music')
		result.export(path)
		with open(path, 'rb') as f:
			instance.short_file.save(os.path.basename(instance.file.name), File(f))
		os.remove(path)