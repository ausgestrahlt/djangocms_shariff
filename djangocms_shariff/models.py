from django.db import models

from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError

from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin 


@python_2_unicode_compatible
class Shariff(CMSPlugin):
    # general settings
    use_backend = models.BooleanField(
        _('Use the shariff backend'),
        default=False
    )
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
    # TODO: email_subject and email_body should be facultative

    def clean(self):
        if self.use_backend:
            try:
                backend = reverse('shariff_backend:get')
            except Exception, e:
                raise ValidationError(
                    {
                        'use_backend': _('It seems the backend is not configured properly.')
                    }
                )

    def __str__(self):
        return 'Shariff' 
