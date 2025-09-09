import json

from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import gettext_lazy as _

from cms.models import CMSPlugin


@python_2_unicode_compatible
class Shariff(CMSPlugin):
    # general settings
    use_backend = models.BooleanField(
        _("Use the shariff backend"),
        default=False,
        help_text=_(
            "The backend will fetch sharing statistics for the respective channels"
        ),
    )

    ORIENTATION_CHOICES = (("vertical", _("vertical")), ("horizontal", _("horizontal")))
    orientation_choices = models.CharField(
        _("orientation"),
        max_length=10,
        choices=ORIENTATION_CHOICES,
        default="horizontal",
    )

    THEME_CHOICES = (
        ("standard", _("standard")),
        ("grey", _("grey")),
        ("white", _("white")),
    )
    theme_choices = models.CharField(
        _("theme"), max_length=8, choices=THEME_CHOICES, default="standard"
    )

    # social media channels
    addthis = models.BooleanField(default=False)
    facebook = models.BooleanField(default=False)
    googleplus = models.BooleanField(default=False)
    linkedin = models.BooleanField(default=False)
    pinterest = models.BooleanField(default=False)
    threema = models.BooleanField(default=False)
    tumblr = models.BooleanField(default=False)
    twitter = models.BooleanField(default=False)
    whatsapp = models.BooleanField(default=False)
    xing = models.BooleanField(default=False)

    info = models.BooleanField(
        default=False, help_text=_("Show info icon next to share buttons")
    )

    # email
    mail = models.BooleanField(help_text=_("Enable sharing via e-mail"))
    mail_subject = models.TextField(_("subject"), blank=True)
    mail_body = models.TextField(_("content"), blank=True)

    def clean(self):
        if self.use_backend:
            try:
                backend = reverse("shariff_backend:get")
            except Exception:
                msg = "It seems the backend is not configured properly."
                raise ValidationError({"use_backend": _(msg)})

    def get_social_choices(self):
        channel_dict = {}
        channel_dict["facebook"] = self.facebook
        channel_dict["twitter"] = self.twitter
        channel_dict["xing"] = self.xing
        channel_dict["googleplus"] = self.googleplus
        channel_dict["linkedin"] = self.linkedin
        channel_dict["pinterest"] = self.pinterest
        channel_dict["whatsapp"] = self.whatsapp
        channel_dict["threema"] = self.threema
        channel_dict["addthis"] = self.addthis
        channel_dict["tumblr"] = self.tumblr
        channel_dict["info"] = self.info
        channel_dict["mail"] = self.mail
        channel_pseudo_list = "["
        for key in channel_dict.keys():
            if channel_dict[key]:
                channel_pseudo_list += "&quot;%s&quot;," % key

        channel_pseudo_list += "]"
        channel_pseudo_list = channel_pseudo_list.replace(",]", "]")
        return channel_pseudo_list

    def __str__(self):
        return "Shariff"
