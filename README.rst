django-themeit
==================

Install
------------------
* python setup.py install

Configure
------------------

* Add themeit.middleware.ThemeitMiddleware to MIDDLEWARE_CLASSES in settings.py
* Add themeit to your INSTALLED_APPS to get the themes-models
* Add themes.py to your project

    themepatterns = {
      "^127.0.0.1":       "1",
    }

* Create theme via admin
* Use the templatetag to render the right css in your .html, ex base.html

    <link rel="stylesheet" href="/site_media/css/{% get_theme %}" type="text/css">