from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class userdata(models.Model):
	name = models.CharField(max_length = 50)
	blog_title = models.CharField(max_length = 200)
	blog_description = models.CharField(max_length = 2000)

	def get_absolute_url(self):
		return reverse('display_usr', kwargs = {'pk':self.pk})

	def __str__(self):
		return self.blog_title + " - " + self.name