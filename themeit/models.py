from django.db import models
from django.contrib.sites.models import Site

class Theme(models.Model):
    css = models.CharField(max_length=255, blank=True, null=True)
    site = models.ForeignKey(Site)
    analytics = models.TextField(blank=True, null=True)
    def __unicode__(self):
        return '%s' % self.site
    class Admin:
        pass
