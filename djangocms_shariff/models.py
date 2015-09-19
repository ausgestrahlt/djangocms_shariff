from django.db import models

from cms.models import CMSPlugin 
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Shariff(CMSPlugin):
    # general settings
    use_backend = models.BooleanField(default=False)
    # TODO: add theme, orientation

    # social media channels
    facebook = models.BooleanField()
    twitter = models.BooleanField()

    # email
    # TODO: rename emailboolean to email
    emailboolean = models.BooleanField()
    # TODO: renmae emailsubject to email_subject
    emailsubject = models.TextField()
    # TODO: erase emailaddress, include email_body
    emailadress = models.CharField(max_length=255)

    def __str__(self):
        return 'Shariff' 
