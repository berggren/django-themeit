"""Admin classes for themeit application."""

from django.contrib import admin

from themeit.models import Example


class ExampleAdmin(admin.ModelAdmin):
    """Admin class for Example model class."""
    pass


admin.site.register(Example, ExampleAdmin)
