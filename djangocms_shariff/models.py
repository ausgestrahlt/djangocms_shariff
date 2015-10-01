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

    ORIENTATION_CHOICES = (
        ('vertical', _('vertical')),
        ('horizontal',_('horizontal')),
        )
    orientation_choices = models.CharField(
        _('orientation'),
        max_length=10,
        choices=ORIENTATION_CHOICES,
        default='horizontal')
    
    THEME_CHOICES = (
        ('standard',_('standard')),
        ('grey',_('grey')),
        ('white',_('white')),
        )
    theme_choices = models.CharField(
        _('theme'),
        max_length=8,
        choices=THEME_CHOICES,
        default='standard')

    # social media channels
    facebook = models.BooleanField(default=False)
    twitter = models.BooleanField(default=False)
    googleplus = models.BooleanField(default=False)
    linkedin = models.BooleanField(default=False)
    pinterest = models.BooleanField(default=False)
    xing = models.BooleanField(default=False)
    whatsapp = models.BooleanField(default=False)
    addthis = models.BooleanField(default=False)
    tumblr = models.BooleanField(default=False)
    info = models.BooleanField(default=False, help_text=_('Provide information about the Plugin'))
    # email
    email = models.BooleanField(help_text=_('Enable sharing via e-mail'))
    email_subject = models.TextField(_('subject'),blank=True)
    email_body = models.TextField(_('content'),blank=True)

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
