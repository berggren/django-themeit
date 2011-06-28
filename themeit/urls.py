"""URLs for themeit application."""

from django.conf.urls.defaults import *


urlpatterns = patterns('themeit.views',
    url(r'^$', view='index', name='themeit_index'),
)
