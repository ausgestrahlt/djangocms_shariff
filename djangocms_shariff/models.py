from django.db import models

from cms.models import CMSPlugin 
from django.utils.encoding import python_2_unicode_compatible



class Shariff(CMSPlugin):
  facebook = models.BooleanField()
  twitter = models.BooleanField()
  emailboolean = models.BooleanField()
  emailsubject = models.TextField()
  emailadress = models.CharField(max_length=255)

  def __str__(self):
    return '' 
