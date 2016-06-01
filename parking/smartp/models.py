from __future__ import unicode_literals

from django.db import models

# Create your models here.

class park(models.Model):
	parking_name = models.CharField(max_length=20)
	parking_no = models.IntegerField()
	status = models.IntegerField(default=0)
	
	def __unicode__(self):
		return  self.name