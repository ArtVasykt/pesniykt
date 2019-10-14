from django.db import models

# Create your models here.
class Singer(models.Model):
	name = models.CharField(max_length=100, blank=True, verbose_name='Прозвище или Имя')
	image = models.ImageField(upload_to='pics',blank=True, verbose_name='Лицо')
	biography = models.TextField(blank=True, verbose_name='Биография')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Исполнитель'
		verbose_name_plural = 'Исполнители'

class Genre(models.Model):
	name = models.CharField(max_length=100, verbose_name='Название')
	singers = models.ManyToManyField(Singer, verbose_name='Самые яркие исполнители')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Жанр'
		verbose_name_plural = 'Жанры'

class Track(models.Model):
	singer = models.ManyToManyField(Singer, verbose_name='Исполнитель(и)')
	genre = models.ForeignKey(Genre, on_delete=models.CASCADE, verbose_name='Жанр')
	name = models.CharField(max_length=100, verbose_name='Название')
	file = models.FileField(upload_to='music', verbose_name='Файл')

	# Подрезка pydub
	short_file = models.FileField(upload_to='short_music', verbose_name='Файл превьюхи', blank=True, default=None, null=True)
	start = models.SmallIntegerField(default=0, blank=True, verbose_name='Начало подрезки')
	end = models.SmallIntegerField(default=0, blank=True, verbose_name='Конец подрезки')

	def __str__(self):
		singers = ''
		for index, singer in enumerate(self.singer.all()):
			singers += singer.name
			if not len(self.singer.all()) == index + 1:
				singers += ' & '
		return '{0} - {1}'.format(singers, self.name)

	class Meta:
		verbose_name = 'Трек'
		verbose_name_plural = 'Треки'
