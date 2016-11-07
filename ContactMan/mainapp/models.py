from __future__ import unicode_literals

from django.db import models

class Contact(models.Model):
	fname = models.CharField(max_length=100)
	lname = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	clnum = models.CharField(max_length=10)
	notes = models.CharField(max_length=1000)
