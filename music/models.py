from django.db import models

from django.core.urlresolvers import reverse
class Album(models.Model):
	
	artist=models.CharField(max_length=250)
	album_title=models.CharField(max_length=250)
	
	album_logo=models.FileField()

	def get_absolute_url(self):       #It creates autopath for whatever album clicked to its detail page
		return reverse('music:detail', kwargs={'pk':self.pk})

	def __str__(self):
		return self.artist+'-'+self.album_title

class song(models.Model):
	album=models.ForeignKey(Album,on_delete=models.CASCADE)
	song_title=models.CharField(max_length=250)
	file_type=models.FileField(null=True)

	def __str__(self):
		return self.song_title

class video(models.Model):
	
	artist=models.CharField(max_length=250)
	video_title=models.CharField(max_length=250)
	video_logo=models.FileField()
	
	def get_absolute_url(self):       #It creates autopath for whatever album clicked to its detail page
		return reverse('music:detailv', kwargs={'pk':self.pk})

	def __str__(self):
		return self.artist+'-'+self.video_title

class document(models.Model):
	document_title=models.CharField(max_length=250)
	doc_url=models.FileField()

	def __str__(self):
		return self.document_title

