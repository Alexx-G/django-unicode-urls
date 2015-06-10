Add unicode urls to your django website.
-------------------------------------------

This module provides patches to support unicode urls in django and django cms.
These patches should be applied in manage.py or wsgi.py files (Monkey patching).

Just add these lines in manage.py/wsgi.py.


::

    from unicode_urls.django import patch_django_urls
    from unicode_urls.cms import patch_djangocms_urls

    patch_django_urls()
    patch_djangocms_urls()


You have to replace cms.urls in your urls config with unicode_urls.cms.urls.

::

    urlpatterns = patterns(
        '',
        # ...
        url(r'^', include('unicode_urls.cms.urls')),
        # ...
    )

