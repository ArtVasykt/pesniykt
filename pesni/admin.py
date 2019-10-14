from django.contrib import admin
from . import models

class TrackAdmin(admin.ModelAdmin):
	list_display = ('name', 'genre')

# Register your models here.
admin.site.register(models.Singer)
admin.site.register(models.Genre)
admin.site.register(models.Track, TrackAdmin)