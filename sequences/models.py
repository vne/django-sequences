from django.db import models
from django.utils.translation import ugettext_lazy as _


class Sequence(models.Model):

    name = models.CharField(
        verbose_name=_("name"),
        max_length=100,
        primary_key=True,
    )

    last = models.BigIntegerField(
        verbose_name=_("last value"),
    )

    class Meta:
        verbose_name = _("sequence")
        verbose_name_plural = _("sequences")

    def __str__(self):
        return "Sequence(name={}, last={})".format(
            repr(self.name), repr(self.last))
