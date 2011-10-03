__author__ = 'jbn'
from django import template
from themeit.models import Theme

register = template.Library()

@register.simple_tag(takes_context=True)
def get_theme(context):
    request = context['request']
    theme = Theme.objects.get(pk=request.themeid)
    return theme.css

@register.simple_tag(takes_context=True)
def get_site(context):
    request = context['request']
    return request.site