from django.db import models

from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError

from django.utils.encoding import python_2_unicode_compatible

from cms.models import CMSPlugin 


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

    def clean(self):
        if self.use_backend:
            backend = reverse('shariff_backend:get')
            import ipdb; ipdb.set_trace()
            raise ValidationError(
                {
                    'use_backend': 'backend not there'
                }
            )

    def __str__(self):
        return 'Shariff' 
